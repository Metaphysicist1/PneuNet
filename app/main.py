from fastapi import FastAPI, Request, UploadFile, File
from fastapi.templating import Jinja2Templates
from fastapi.testclient import TestClient

from PIL import Image
import tensorflow as tf

import uvicorn

from app.logger import logger

import numpy as np
import io
import os
import dotenv

import mlflow

dotenv.load_dotenv()

DATABRICKS_HOST = os.environ["DATABRICKS_HOST"]
DATABRICKS_TOKEN = os.environ["DATABRICKS_TOKEN"]

mlflow.set_tracking_uri("databricks")
mlflow.set_experiment("/Users/edgarabasov1@gmail.com/image_classification/")

app = FastAPI(title="Pneumonia Detection")

templates = Jinja2Templates(directory="app/templates")

MODEL_PATH = "scripts/models/best_mobilenetv2.h5"
IMG_HEIGHT = 224
IMG_WIDTH = 224
model = None

@app.on_event("startup")
async def startup_event():
    global model 
    logger.info("Application starting up")
    try:
        # Create model with proper Lambda layer
        model = create_model()
        
        # Check if model file exists
        if os.path.exists(MODEL_PATH):
            # Load weights
            model.load_weights(MODEL_PATH)
            logger.info(f"Model weights loaded successfully from {MODEL_PATH}")
        else:
            logger.warning(f"Model file not found at {MODEL_PATH}, using untrained model")
    except Exception as e:
        logger.error(f"Error loading model: {e}")
        model = None

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Application shutting down")

@app.get("/")
async def home(request: Request):
    logger.info("Home page requested")
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    logger.info(f"Prediction requested for file: {file.filename}")
    
    if not model:
        logger.error("Model not loaded")
        return {"error": "Model not loaded"}

    try:
        content = await file.read()
        image = Image.open(io.BytesIO(content)).convert("L")  # Convert to grayscale
        image = image.resize((IMG_HEIGHT, IMG_WIDTH))

        img_array = np.array(image)
        img_array = img_array / 255.0 

        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
        img_array = np.expand_dims(img_array, axis=-1)  # Add channel dimension for grayscale
        
        with mlflow.start_run():
            mlflow.sklearn.log_model(model, "my_model")

            # Make prediction
            prediction = model.predict(img_array)
            probability = float(prediction[0][0])
            
            threshold = 0.5
            diagnosis = "Pneumonia" if probability > threshold else "Normal"
            
            logger.info(f"Prediction complete: {diagnosis} with probability {probability:.4f}")
            
            return {
                "filename": file.filename,
                "diagnosis": diagnosis,
                "probability": probability,
                "threshold_used": threshold
            }
    except Exception as e:
        logger.error(f"Error processing image: {e}")
        return {"error": f"Invalid image: {str(e)}"}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "model_loaded": model is not None}

if __name__ == "__main__":
    logger.info("Starting application with uvicorn")
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)