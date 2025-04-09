from fastapi.testclient import TestClient
from app.main import app
import os
from pathlib import Path
from app.logger import setup_logger

# Set up a test-specific logger
logger = setup_logger("test")

# Create templates directory if it doesn't exist
templates_dir = Path("app/templates")
templates_dir.mkdir(exist_ok=True, parents=True)

# Create a simple index.html template if it doesn't exist
index_html = templates_dir / "index.html"
if not index_html.exists():
    logger.info("Creating test index.html template")
    with open(index_html, "w") as f:
        f.write("<!DOCTYPE html><html><body><h1>Test Page</h1></body></html>")

# Initialize TestClient
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
    