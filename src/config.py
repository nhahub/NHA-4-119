"""Configuration settings for the FastAPI application."""

from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional, List


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # API Configuration
    api_key: str = "dev-api-key-change-in-production"
    api_version: str = "v1"

    # Application Configuration
    app_name: str = "Content Generation API"
    app_description: str = "AI-powered text content generation for blog posts and articles"
    debug: bool = False

    # Logging
    log_level: str = "INFO"

    # CORS (stored as string, parsed when used)
    cors_origins: str = "*"

    # Model Configuration (for ML integration)
    model_path: Optional[str] = None
    model_name: str = "gpt2-medium"
    max_tokens: int = 200
    temperature: float = 0.7
    top_p: float = 0.9

    # Server Configuration
    host: str = "0.0.0.0"
    port: int = 8000

    @property
    def cors_origins_list(self) -> List[str]:
        """Parse CORS origins from string to list."""
        if self.cors_origins.strip() == '*':
            return ["*"]
        return [origin.strip() for origin in self.cors_origins.split(',') if origin.strip()]


# Create singleton instance
settings = Settings()