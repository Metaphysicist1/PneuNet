import sys
import pytest
from fastapi.testclient import TestClient

# Import app directly
from app.main import app

client = TestClient(app)

def test_read_main():
    """Test that the main route returns 200 OK"""
    response = client.get("/")
    assert response.status_code == 200

def test_health_check():
    """Test that the health check route returns 200 OK"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    assert "tensorflow_available" in response.json()

def test_predict_no_file():
    """Test that trying to predict without a file returns 422"""
    response = client.post("/predict")
    assert response.status_code == 422  # Validation error

def test_predict_invalid_file():
    """Test that trying to predict with an invalid file returns an error"""
    response = client.post(
        "/predict",
        files={"file": ("filename", b"invalid file content", "image/jpeg")}
    )
    assert response.status_code == 200
    assert "error" in response.json()