"""Pydantic schemas for request/response models."""

from pydantic import BaseModel, Field
from typing import Optional


class GenerationRequest(BaseModel):
    """Request model for text content generation endpoint."""

    topic: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="Main topic or title for the content",
        examples=["Benefits of Remote Work"]
    )
    content_type: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Type of content: blog, post, article, etc.",
        examples=["blog"]
    )
    style: Optional[str] = Field(
        default="informative",
        description="Writing style: informative, casual, professional, etc.",
        examples=["informative"]
    )
    keywords: Optional[list[str]] = Field(
        default=None,
        description="Keywords to include in the content",
        examples=[["remote work", "productivity", "work-life balance"]]
    )
    max_tokens: Optional[int] = Field(
        default=500,
        ge=50,
        le=2000,
        description="Maximum number of tokens to generate"
    )




