"""Health check router."""

import time
from fastapi import APIRouter, status
from src.api.schemas import HealthResponse

# Router instance
router = APIRouter(tags=["health"])

# Application start time (to be set by main.py)
app_start_time: float = 0
model_loaded: bool = False


@router.get(
    "/health",
    response_model=HealthResponse,
    status_code=status.HTTP_200_OK,
    summary="Health Check",
    description="Check the health status of the API and model availability",
)
async def health_check() -> HealthResponse:
    """Health check endpoint that returns API status and model availability."""
    uptime = int(time.time() - app_start_time) if app_start_time > 0 else 0
    
    return HealthResponse(
        status="ok" if model_loaded else "starting",
        model_loaded=model_loaded,
        uptime_seconds=uptime,
    )


def set_app_start_time(start_time: float) -> None:
    """Set the application start time."""
    global app_start_time
    app_start_time = start_time


def set_model_loaded(loaded: bool) -> None:
    """Set the model loaded status."""
    global model_loaded
    model_loaded = loaded