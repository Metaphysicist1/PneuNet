from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn
from fastapi.testclient import TestClient
from app.logger import logger


app = FastAPI(title="Test App")

templates = Jinja2Templates(directory="app/templates")


@app.on_event("startup")
async def startup_event():
    logger.info("Application starting up")


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Application shutting down")


@app.get("/")
async def home(request: Request):
    logger.info("Home page requested")
    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == "__main__":
    logger.info("Starting application with uvicorn")
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)