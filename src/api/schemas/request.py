"""Pydantic schemas for request/response models."""

from pydantic import BaseModel, Field
from typing import Literal, Optional


class GenerationRequest(BaseModel):
    """Request model for text content generation endpoint."""

    topic: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="Main topic or title for the content",
        examples=["Benefits of Remote Work"]
    )
    content_type: Literal["blog", "linkedin", "tweet", "instagram", "short_story"] = Field(
        ...,
        description="Type of content to generate with the agent pipeline.",
        examples=["blog"]
    )
    audience: Optional[str] = Field(
        default=None,
        max_length=200,
        description="Target audience for the generated content.",
        examples=["Marketing professionals"]
    )
    tone: Literal[
        "professional",
        "casual",
        "witty",
        "inspirational",
        "educational",
        "neutral",
    ] = Field(
        default="professional",
        description="Tone used by the writer agent.",
        examples=["professional"]
    )
    brief: Optional[str] = Field(
        default=None,
        max_length=2000,
        description="Optional creative or business instructions for the agents.",
    )
    reference_text: Optional[str] = Field(
        default=None,
        max_length=5000,
        description="Optional source text or inspiration to guide the output.",
    )
    max_tokens: Optional[int] = Field(
        default=500,
        ge=50,
        le=2000,
        description="Maximum number of tokens the frontend wants to allow for generation."
    )

