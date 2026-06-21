"""Tests for health check endpoint."""

import pytest
from fastapi.testclient import TestClient


def test_health_check(client: TestClient):
    """Test that health check returns 200 and correct structure."""
    response = client.get("/health")
    
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert "model_loaded" in data
    assert "uptime_seconds" in data


def test_health_check_status_values(client: TestClient):
    """Test that health check returns valid status values."""
    response = client.get("/health")
    
    assert response.status_code == 200
    data = response.json()
    
    # Status should be one of: ok, starting, error
    assert data["status"] in ["ok", "starting", "error"]
    
    # model_loaded should be a boolean
    assert isinstance(data["model_loaded"], bool)
    
    # uptime_seconds should be a non-negative integer
    assert isinstance(data["uptime_seconds"], int)
    assert data["uptime_seconds"] >= 0