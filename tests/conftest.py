"""Pytest configuration and fixtures."""

import pytest
from fastapi.testclient import TestClient
from src.api.main import app


@pytest.fixture
def client():
    """Create a test client for the FastAPI application."""
    return TestClient(app)


@pytest.fixture
def valid_api_key():
    """Return a valid API key for testing."""
    return "dev-api-key-change-in-production"


@pytest.fixture
def invalid_api_key():
    """Return an invalid API key for testing."""
    return "invalid-key"


@pytest.fixture
def generation_request():
    """Return a valid generation request payload."""
    return {
        "topic": "Benefits of Remote Work",
        "content_type": "blog",
        "style": "informative",
        "keywords": ["remote work", "productivity", "work-life balance"],
        "max_tokens": 500,
    }