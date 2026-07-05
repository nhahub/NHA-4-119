"""Job tracking backed by the database, with a local memory fallback."""

import os
from copy import deepcopy
from datetime import datetime, timezone
from threading import RLock
from typing import Any
from uuid import uuid4

from sqlalchemy.exc import SQLAlchemyError

from src.database.database import SessionLocal
from src.models import (
    ContentGeneration,
    GeneratedContent,
    GenerationDebugData,
    GenerationJob,
)


class JobStore:
    """Store background generation jobs for polling and result retrieval.

    In production this writes to the configured SQL database, so jobs survive
    app restarts and can be inspected from a hosted Postgres dashboard. During
    local setup, if the database is unreachable or migrations have not run yet,
    it falls back to memory so the API can still be tested.
    """

    def __init__(self) -> None:
        self._memory_jobs: dict[str, dict[str, Any]] = {}
        self._lock = RLock()
        self._database_available: bool | None = None
        self._strict_database = os.getenv("JOB_STORE_STRICT_DATABASE", "false").lower() == "true"

    def create(self, request_payload: dict[str, Any], user_id: str | None = None) -> dict[str, Any]:
        """Create a queued generation job."""
        now = self._now_datetime()
        job_id = str(uuid4())
        job_data = {
            "job_id": job_id,
            "user_id": user_id,
            "status": "queued",
            "progress": 0,
            "message": "Job queued",
            "request": request_payload,
            "result": None,
            "error": None,
            "created_at": self._to_iso(now),
            "updated_at": self._to_iso(now),
            "completed_at": None,
        }

        if self._use_database():
            try:
                with SessionLocal() as session:
                    row = GenerationJob(
                        id=job_id,
                        user_id=user_id,
                        status="queued",
                        progress=0,
                        message="Job queued",
                        request_payload=request_payload,
                        created_at=now,
                        updated_at=now,
                    )
                    session.add(row)
                    session.add(self._build_content_generation(job_id, user_id, request_payload, now))
                    session.commit()
                    session.refresh(row)
                    self._database_available = True
                    return self._row_to_dict(row)
            except SQLAlchemyError:
                self._handle_database_failure()

        return self._memory_create(job_data)

    def get(self, job_id: str) -> dict[str, Any] | None:
        """Fetch a job by ID from the database or fallback memory store."""
        if self._use_database():
            try:
                with SessionLocal() as session:
                    row = session.get(GenerationJob, job_id)
                    self._database_available = True
                    return self._row_to_dict(row) if row else None
            except SQLAlchemyError:
                self._handle_database_failure()

        return self._memory_get(job_id)

    def update(self, job_id: str, **changes: Any) -> dict[str, Any] | None:
        """Patch lifecycle fields as the background worker progresses."""
        if self._use_database():
            try:
                with SessionLocal() as session:
                    row = session.get(GenerationJob, job_id)
                    if not row:
                        return None

                    self._apply_changes(row, changes)
                    self._sync_generation_records(session, row, changes)
                    session.commit()
                    session.refresh(row)
                    self._database_available = True
                    return self._row_to_dict(row)
            except SQLAlchemyError:
                self._handle_database_failure()

        return self._memory_update(job_id, **changes)

    def _use_database(self) -> bool:
        """Use DB until it fails once; strict mode raises instead of falling back."""
        return self._database_available is not False

    def _handle_database_failure(self) -> None:
        """Switch to memory unless strict database mode is enabled."""
        if self._strict_database:
            raise
        self._database_available = False

    @staticmethod
    def _apply_changes(row: GenerationJob, changes: dict[str, Any]) -> None:
        """Map public job fields onto database columns."""
        if "status" in changes:
            row.status = changes["status"]
            if changes["status"] in {"completed", "failed"}:
                row.completed_at = JobStore._now_datetime()
        if "progress" in changes:
            row.progress = changes["progress"]
        if "message" in changes:
            row.message = changes["message"]
        if "result" in changes:
            row.result_payload = changes["result"]
        if "error" in changes:
            row.error = changes["error"]
        row.updated_at = JobStore._now_datetime()

    @staticmethod
    def _build_content_generation(
        job_id: str,
        user_id: str | None,
        request_payload: dict[str, Any],
        now: datetime,
    ) -> ContentGeneration:
        """Create the normalized request row tied to the background job."""
        return ContentGeneration(
            id=str(uuid4()),
            user_id=user_id,
            job_id=job_id,
            topic=request_payload["topic"],
            content_type=request_payload["content_type"],
            audience=request_payload.get("audience"),
            tone=request_payload.get("tone", "professional"),
            brief=request_payload.get("brief"),
            reference_text=request_payload.get("reference_text"),
            max_tokens=request_payload.get("max_tokens"),
            status="queued",
            created_at=now,
            updated_at=now,
        )

    @staticmethod
    def _sync_generation_records(session, row: GenerationJob, changes: dict[str, Any]) -> None:
        """Keep normalized generation/content/debug rows in sync with job state."""
        generation = (
            session.query(ContentGeneration)
            .filter(ContentGeneration.job_id == row.id)
            .one_or_none()
        )
        if not generation:
            return

        if "status" in changes:
            generation.status = changes["status"]
            generation.updated_at = JobStore._now_datetime()

        result = changes.get("result")
        if changes.get("status") == "completed" and isinstance(result, dict):
            JobStore._upsert_generated_content(session, generation, row, result)
            JobStore._upsert_debug_data(session, generation, row, result)

    @staticmethod
    def _upsert_generated_content(
        session,
        generation: ContentGeneration,
        row: GenerationJob,
        result: dict[str, Any],
    ) -> None:
        """Save the clean final content in its own table."""
        existing = (
            session.query(GeneratedContent)
            .filter(GeneratedContent.generation_id == generation.id)
            .one_or_none()
        )
        draft = result.get("draft") or {}
        content = result.get("content") or ""
        now = JobStore._now_datetime()
        values = {
            "user_id": row.user_id,
            "generation_id": generation.id,
            "title": draft.get("selected_title"),
            "content": content,
            "content_type": result.get("content_type"),
            "active_writer": result.get("active_writer"),
            "revision_count": result.get("revision_count", 0),
            "word_count": JobStore._extract_word_count(draft, content),
            "metadata_json": {
                "job_id": row.id,
                "citations_used": draft.get("citations_used"),
                "hashtags": draft.get("hashtags") or draft.get("hashtags_used"),
            },
            "updated_at": now,
        }

        if existing:
            for key, value in values.items():
                setattr(existing, key, value)
            return

        session.add(
            GeneratedContent(
                id=str(uuid4()),
                created_at=now,
                **values,
            )
        )

    @staticmethod
    def _upsert_debug_data(
        session,
        generation: ContentGeneration,
        row: GenerationJob,
        result: dict[str, Any],
    ) -> None:
        """Save agent internals separately from user-facing content."""
        existing = (
            session.query(GenerationDebugData)
            .filter(GenerationDebugData.generation_id == generation.id)
            .one_or_none()
        )
        values = {
            "user_id": row.user_id,
            "generation_id": generation.id,
            "outline_payload": result.get("outline"),
            "search_payload": result.get("search"),
            "draft_payload": result.get("draft"),
            "critique_payload": result.get("critique"),
        }

        if existing:
            for key, value in values.items():
                setattr(existing, key, value)
            return

        session.add(
            GenerationDebugData(
                id=str(uuid4()),
                created_at=JobStore._now_datetime(),
                **values,
            )
        )

    @staticmethod
    def _extract_word_count(draft: dict[str, Any], content: str) -> int | None:
        """Use writer-provided counts first, then fall back to splitting content."""
        for key in ("word_count", "caption_word_count"):
            if isinstance(draft.get(key), int):
                return draft[key]
        return len(content.split()) if content else None

    def _memory_create(self, job_data: dict[str, Any]) -> dict[str, Any]:
        with self._lock:
            self._memory_jobs[job_data["job_id"]] = job_data
        return deepcopy(job_data)

    def _memory_get(self, job_id: str) -> dict[str, Any] | None:
        with self._lock:
            job = self._memory_jobs.get(job_id)
            return deepcopy(job) if job else None

    def _memory_update(self, job_id: str, **changes: Any) -> dict[str, Any] | None:
        with self._lock:
            job = self._memory_jobs.get(job_id)
            if not job:
                return None

            job.update(changes)
            job["updated_at"] = self._to_iso(self._now_datetime())
            if changes.get("status") in {"completed", "failed"}:
                job["completed_at"] = self._to_iso(self._now_datetime())
            return deepcopy(job)

    @staticmethod
    def _row_to_dict(row: GenerationJob) -> dict[str, Any]:
        """Convert an ORM row into the API's existing job dictionary shape."""
        return {
            "job_id": row.id,
            "user_id": row.user_id,
            "status": row.status,
            "progress": row.progress,
            "message": row.message,
            "request": row.request_payload,
            "result": row.result_payload,
            "error": row.error,
            "created_at": JobStore._to_iso(row.created_at),
            "updated_at": JobStore._to_iso(row.updated_at),
            "completed_at": JobStore._to_iso(row.completed_at),
        }

    @staticmethod
    def _now_datetime() -> datetime:
        """Use UTC for database and API timestamps."""
        return datetime.now(timezone.utc)

    @staticmethod
    def _to_iso(value: datetime | None) -> str | None:
        """Serialize datetimes consistently for JSON responses."""
        return value.isoformat() if value else None


job_store = JobStore()
