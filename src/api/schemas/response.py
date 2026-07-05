"""Pydantic schemas for response models."""

from pydantic import BaseModel, Field
from typing import Any, Literal, Optional


class GenerationResponse(BaseModel):
    """Response model for text content generation endpoint."""

    content: str = Field(
        ...,
        description="Generated text content"
    )
    model_version: str = Field(
        ...,
        description="Version of the model used for generation"
    )
    generation_time_ms: int = Field(
        ...,
        description="Time taken to generate the content in milliseconds"
    )


class GenerationJobResponse(BaseModel):
    """Response returned immediately after a background job is queued."""

    job_id: str = Field(..., description="Unique ID used to poll this job")
    status: Literal["queued"] = Field(..., description="Initial job status")
    status_url: str = Field(..., description="Endpoint for polling job status")
    result_url: str = Field(..., description="Endpoint for reading the final result")
    debug_url: str = Field(..., description="Endpoint for inspecting agent details")


class JobStatusResponse(BaseModel):
    """Current lifecycle state for a background generation job."""

    job_id: str
    status: Literal["queued", "running", "completed", "failed"]
    progress: int = Field(..., ge=0, le=100)
    message: str
    error: Optional[str] = None
    created_at: str
    updated_at: str


class JobResultResponse(BaseModel):
    """Clean final content returned after a generation job completes."""

    job_id: str
    status: Literal["completed"]
    content: str
    content_type: Optional[str] = None
    active_writer: Optional[str] = None
    revision_count: int = 0


class JobDebugResponse(BaseModel):
    """Full normalized agent output for debugging and development."""

    job_id: str
    status: Literal["completed"]
    debug: dict[str, Any]


class HealthResponse(BaseModel):
    """Response model for health check endpoint."""

    status: str = Field(
        ...,
        description="Health status: ok, starting, or error",
        examples=["ok"]
    )
    model_loaded: bool = Field(
        ...,
        description="Whether the model is loaded and ready"
    )
    uptime_seconds: int = Field(
        ...,
        description="Uptime of the application in seconds"
    )


class ErrorResponse(BaseModel):
    """Response model for error responses."""

    detail: str = Field(
        ...,
        description="Error message"
    )
    error_code: Optional[str] = Field(
        default=None,
        description="Error code for programmatic error handling"
    )
