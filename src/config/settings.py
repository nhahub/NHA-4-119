"""Configuration settings for the FastAPI application."""

from typing import List, Optional

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # API configuration
    api_key: str = "dev-api-key-change-in-production"
    api_version: str = "v1"

    # Application metadata
    app_name: str = "LEXORA Content Generation API"
    app_description: str = "AI-powered text content generation for blog posts and articles"
    debug: bool = False

    @field_validator("debug", mode="before")
    @classmethod
    def parse_debug(cls, value):
        """Accept deployment words like `release` in addition to booleans."""
        if isinstance(value, str) and value.lower() in {"release", "prod", "production"}:
            return False
        return value

    # Logging
    log_level: str = "INFO"

    # CORS is stored as a string in .env, then parsed for FastAPI.
    cors_origins: str = "*"

    # Kept for compatibility with older local-model code paths.
    model_path: Optional[str] = None
    model_name: str = "gpt2-medium"
    max_tokens: int = 200
    temperature: float = 0.7
    top_p: float = 0.9

    # Server configuration
    host: str = "0.0.0.0"
    port: int = 8000

    @property
    def cors_origins_list(self) -> List[str]:
        """Convert comma-separated CORS origins into FastAPI's list format."""
        if self.cors_origins.strip() == "*":
            return ["*"]
        return [
            origin.strip()
            for origin in self.cors_origins.split(",")
            if origin.strip()
        ]


settings = Settings()
