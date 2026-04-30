"""Pydantic schemas for response models."""

from pydantic import BaseModel, Field
from typing import Optional


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