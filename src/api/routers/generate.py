"""Generation router for text content generation."""

import time
from fastapi import APIRouter, HTTPException, status
from src.api.schemas import GenerationRequest, GenerationResponse
from src.api.services.generation_service import generation_service

# Router instance
router = APIRouter(prefix="/api/v1", tags=["generation"])


@router.post(
    "/generate",
    response_model=GenerationResponse,
    status_code=status.HTTP_200_OK,
    summary="Generate Text Content",
    description="Generate text content like blog posts or articles using the AI model",
    responses={
        422: {"description": "Validation Error"},
        500: {"description": "Internal Server Error"},
    },
)
async def generate_content(request: GenerationRequest) -> GenerationResponse:
    """
    Generate text content based on the provided details.
    
    - **topic**: Main topic or title for the content (required)
    - **content_type**: Type of content: blog, post, article, etc. (required)
    - **style**: Writing style: informative, casual, professional, etc. (optional)
    - **keywords**: Keywords to include in the content (optional)
    - **max_tokens**: Maximum tokens to generate (optional, default 500)
    """
    start_time = time.time()
    
    try:
        # Generate content using the service
        content = await generation_service.generate(
            topic=request.topic,
            content_type=request.content_type,
            style=request.style,
            keywords=request.keywords,
            max_tokens=request.max_tokens,
        )
        
        # Calculate generation time
        generation_time_ms = int((time.time() - start_time) * 1000)
        
        return GenerationResponse(
            content=content,
            model_version="v1.0",
            generation_time_ms=generation_time_ms,
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error generating content: {str(e)}",
        )