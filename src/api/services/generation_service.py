"""Generation service for text content generation."""

import logging

from typing import Optional


logger = logging.getLogger(__name__)


class GenerationService:
    """Service for handling text generation requests."""
    
    def __init__(self):
        self.model = None
        self.tokenizer = None
        self.model_loaded = False
        self.model_version = "v1.0"
    
    
    async def generate(
        self,
        topic: str,
        content_type: str,
        style: Optional[str] = None,
        keywords: Optional[list[str]] = None,
        max_tokens: int = 500,
    ) -> str:
        """
        Generate text content using local model.
        
        Args:
            topic: Main topic or title for the content
            content_type: Type of content: blog, post, article, etc.
            style: Writing style: informative, casual, professional, etc.
            keywords: Keywords to include in the content
            max_tokens: Maximum tokens to generate
            
        Returns:
            Generated text content
        """
        logger.info(
            f"Generating {content_type} content for topic: {topic}"
        )
        
        if not self.model_loaded:
            raise RuntimeError("Model not loaded. Please load the model first.")
        
        # Build the prompt
        prompt = self._build_prompt(topic, content_type, style, keywords)
        
        # Generate content using local model
        content = self._generate_with_model(prompt, max_tokens)
        
        return content
    
    def _build_prompt(
        self,
        topic: str,
        content_type: str,
        style: Optional[str] = None,
        keywords: Optional[list[str]] = None,
    ) -> str:
        """Build the prompt for the model."""
        prompt = f"Topic: {topic} | Type: {content_type}"
        
        if style:
            prompt += f" | Style: {style}"
        
        if keywords:
            keywords_str = ", ".join(keywords)
            prompt += f" | Keywords: {keywords_str}"
        
        prompt += " | Content:"
        return prompt
    
   
    
    def set_model_loaded(self, loaded: bool) -> None:
        """Set the model loaded status."""
        self.model_loaded = loaded
    
    def is_model_loaded(self) -> bool:
        """Check if the model is loaded."""
        return self.model_loaded


# Create singleton instance
generation_service = GenerationService()


