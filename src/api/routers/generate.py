"""Generation router that queues agent pipeline work in the background."""

from fastapi import APIRouter, BackgroundTasks, Header, status

from src.api.schemas import GenerationJobResponse, GenerationRequest
from src.api.services.agent_generation_service import agent_generation_service
from src.api.services.job_store import job_store


router = APIRouter(prefix="/api/v1", tags=["generation"])


@router.post(
    "/generate",
    response_model=GenerationJobResponse,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Queue Text Content Generation",
    description="Queue an agent-based generation job and return immediately.",
    responses={
        202: {"description": "Generation job queued"},
        422: {"description": "Validation Error"},
    },
)
async def generate_content(
    request: GenerationRequest,
    background_tasks: BackgroundTasks,
    user_id: str | None = Header(default=None, alias="X-User-Id"),
) -> GenerationJobResponse:
    """Create a background job so the frontend does not wait for the full flow."""
    job = job_store.create(request.model_dump(), user_id=user_id)
    job_id = job["job_id"]

    # FastAPI runs this after sending the 202 response, avoiding client timeouts.
    background_tasks.add_task(agent_generation_service.run_job, job_id, request)

    return GenerationJobResponse(
        job_id=job_id,
        status="queued",
        status_url=f"/api/v1/jobs/{job_id}",
        result_url=f"/api/v1/jobs/{job_id}/result",
        debug_url=f"/api/v1/jobs/{job_id}/debug",
    )
