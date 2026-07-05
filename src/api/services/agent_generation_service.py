"""Service that runs the LangGraph agent pipeline for a background job."""

import logging
from threading import Lock
from typing import Any

from src.api.schemas import GenerationRequest
from src.api.services.job_store import job_store


logger = logging.getLogger(__name__)


class AgentGenerationService:
    """Bridge between FastAPI jobs and the existing agents graph."""

    def __init__(self) -> None:
        self._app = None
        self._lock = Lock()

    def run_job(self, job_id: str, request: GenerationRequest) -> None:
        """Run one generation job and persist its final state in the job store."""
        try:
            job_store.update(
                job_id,
                status="running",
                progress=10,
                message="Preparing agent context",
            )

            state = self._build_initial_state(job_id, request)
            app = self._get_graph_app()

            job_store.update(
                job_id,
                progress=30,
                message="Running outline, research, writer, and critique agents",
            )

            result = app.invoke(state)
            normalized_result = self._normalize_result(result)

            job_store.update(
                job_id,
                status="completed",
                progress=100,
                message="Generation completed",
                result=normalized_result,
            )
        except Exception as exc:
            logger.exception("Generation job %s failed", job_id)
            job_store.update(
                job_id,
                status="failed",
                progress=100,
                message="Generation failed",
                error=str(exc),
            )

    def _get_graph_app(self):
        """Compile the LangGraph app once and reuse it for later jobs."""
        if self._app is None:
            with self._lock:
                if self._app is None:
                    from src.agents.graph import build_graph

                    self._app = build_graph()
        return self._app

    @staticmethod
    def _build_initial_state(job_id: str, request: GenerationRequest) -> dict[str, Any]:
        """Translate the public API request into the shared agent Context."""
        return {
            "job_id": job_id,
            "topic": request.topic,
            "audience": request.audience,
            "tone": request.tone,
            "content_type": request.content_type,
            "brief": request.brief,
            "reference_text": request.reference_text,
            "outline": {},
            "search": {},
            "active_writer": "",
            "draft": {},
            "critique": {},
            "revision_count": 0,
            "final_content": "",
        }

    @staticmethod
    def _normalize_result(result: dict[str, Any]) -> dict[str, Any]:
        """Expose a stable response shape even though writer outputs differ."""
        draft = result.get("draft") or {}
        content = AgentGenerationService._extract_content(draft)

        return {
            "content": content,
            "content_type": result.get("content_type"),
            "active_writer": result.get("active_writer"),
            "draft": draft,
            "outline": result.get("outline") or {},
            "search": result.get("search") or {},
            "critique": result.get("critique") or {},
            "revision_count": result.get("revision_count", 0),
        }

    @staticmethod
    def _extract_content(draft: dict[str, Any]) -> str:
        """Convert blog/post/thread/story drafts into one frontend-friendly string."""
        body = draft.get("body", "")

        if isinstance(body, list):
            return "\n\n".join(str(item) for item in body)

        if isinstance(body, str):
            title = draft.get("selected_title")
            if title:
                return f"{title}\n\n{body}"
            return body

        return ""


agent_generation_service = AgentGenerationService()
