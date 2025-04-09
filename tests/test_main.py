from fastapi.testclient import TestClient
from app.main import app
from app.logger import setup_logger

# Set up a test-specific logger
logger = setup_logger("test")

client = TestClient(app)


def test_read_app():
    """Test the home endpoint returns HTML template."""
    logger.info("Testing home endpoint")
    response = client.get("/")
    logger.info(f"Response status code: {response.status_code}")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "<!DOCTYPE html>" in response.text
    logger.info("Home endpoint test passed")
    