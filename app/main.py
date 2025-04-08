from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

# Set up templates
templates = Jinja2Templates(directory="app/templates")

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/v1/")
async def api_root():
    return {"message": "Welcome to Pneunet API", "status": "active"}