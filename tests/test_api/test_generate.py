"""Tests for generation endpoint."""

import pytest
from fastapi.testclient import TestClient






def test_generate_minimal_request(client: TestClient, valid_api_key):
    """Test generation with minimal required fields."""
    request = {
        "topic": "Test Topic",
        "content_type": "blog",
    }
    
    response = client.post(
        "/api/v1/generate",
        json=request,
        headers={"X-API-Key": valid_api_key},
    )
    
    assert response.status_code == 200
    data = response.json()
    assert "content" in data


def test_generate_missing_topic(client: TestClient, valid_api_key):
    """Test that missing topic returns 422."""
    request = {
        "content_type": "blog",
    }
    
    response = client.post(
        "/api/v1/generate",
        json=request,
        headers={"X-API-Key": valid_api_key},
    )
    
    assert response.status_code == 422


def test_generate_missing_content_type(client: TestClient, valid_api_key):
    """Test that missing content_type returns 422."""
    request = {
        "topic": "Test Topic",
    }
    
    response = client.post(
        "/api/v1/generate",
        json=request,
        headers={"X-API-Key": valid_api_key},
    )
    
    assert response.status_code == 422


def test_generate_invalid_max_tokens(client: TestClient, valid_api_key):
    """Test that invalid max_tokens returns 422."""
    request = {
        "topic": "Test Topic",
        "content_type": "blog",
        "max_tokens": 3000,  # Above the max limit
    }
    
    response = client.post(
        "/api/v1/generate",
        json=request,
        headers={"X-API-Key": valid_api_key},
    )
    
    assert response.status_code == 422