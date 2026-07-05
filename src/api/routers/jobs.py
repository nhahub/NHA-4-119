"""Job polling endpoints for background generation."""

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

from src.api.schemas import JobDebugResponse, JobResultResponse, JobStatusResponse
from src.api.services.job_store import job_store


router = APIRouter(prefix="/api/v1/jobs", tags=["jobs"])


@router.get(
    "/{job_id}",
    response_model=JobStatusResponse,
    status_code=status.HTTP_200_OK,
    summary="Get Generation Job Status",
)
async def get_job_status(job_id: str) -> JobStatusResponse:
    """Return only lightweight status data for polling UIs."""
    job = _get_job_or_404(job_id)

    return JobStatusResponse(
        job_id=job["job_id"],
        status=job["status"],
        progress=job["progress"],
        message=job["message"],
        error=job["error"],
        created_at=job["created_at"],
        updated_at=job["updated_at"],
    )


@router.get(
    "/{job_id}/result",
    response_model=JobResultResponse,
    status_code=status.HTTP_200_OK,
    summary="Get Generation Job Result",
)
async def get_job_result(job_id: str):
    """Return clean generated content, or a non-error 202 while still active."""
    job = _get_job_or_404(job_id)
    pending_response = _pending_response_or_raise(job)
    if pending_response:
        return pending_response

    result = job["result"] or {}

    return JobResultResponse(
        job_id=job["job_id"],
        status="completed",
        content=result.get("content", ""),
        content_type=result.get("content_type"),
        active_writer=result.get("active_writer"),
        revision_count=result.get("revision_count", 0),
    )


@router.get(
    "/{job_id}/debug",
    response_model=JobDebugResponse,
    status_code=status.HTTP_200_OK,
    summary="Get Generation Job Debug Details",
)
async def get_job_debug(job_id: str):
    """Return the normalized agent state for debugging generation quality."""
    job = _get_job_or_404(job_id)
    pending_response = _pending_response_or_raise(job)
    if pending_response:
        return pending_response

    return JobDebugResponse(
        job_id=job["job_id"],
        status="completed",
        debug=job["result"] or {},
    )


def _get_job_or_404(job_id: str) -> dict:
    """Keep not-found behavior consistent across job endpoints."""
    job = job_store.get(job_id)
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job not found",
        )
    return job


def _pending_response_or_raise(job: dict) -> JSONResponse | None:
    """Share active/failed job behavior between result and debug endpoints."""
    job_id = job["job_id"]

    if job["status"] in {"queued", "running"}:
        return JSONResponse(
            status_code=status.HTTP_202_ACCEPTED,
            content={
                "job_id": job_id,
                "status": job["status"],
                "message": job["message"],
                "status_url": f"/api/v1/jobs/{job_id}",
            },
        )

    if job["status"] == "failed":
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=job["error"] or "Generation job failed",
        )

    return None
