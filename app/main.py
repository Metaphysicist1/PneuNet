from fastapi import FastAPI, Request, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.testclient import TestClient
import tensorflow as tf
import uvicorn

from app.logger import logger

from PIL import Image
import numpy as np
import io

app = FastAPI(title="Test App")

templates = Jinja2Templates(directory="app/templates")

MODEL_PATH = "scripts/models/best_mobilenetv2.h5"
model = None

@app.on_event("startup")
async def startup_event():
    global model 
    logger.info("Application starting up")
    try:
        model = tf.keras.models.load_model(MODEL_PATH)
        logger.info(f"Model loaded successfully from {MODEL_PATH}")
    except Exception as e:
        logger.error(f"Error loading model: {e}")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Application shutting down")


@app.get("/")
async def home(request: Request):
    logger.info("Home page requested")
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
async def predict(file: UploadFile):
    logger.info(f"Prediction requested for file: {file.filename}")
    
    if not model:
        logger.error("Model not loaded")
        return {"error": "Model not loaded"}

    try:
        content = await file.read()
        image = Image.open(io.BytesIO(content)).convert("RGB")
        image = image.resize((224, 224))

        img_array = np.array(image)
        img_array = img_array / 255.0 

        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
        img_array = np.expand_dims(img_array, axis=-1)  # Add channel dimension for grayscale
        
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
        return {"error": "Invalid image"}

if __name__ == "__main__":
    logger.info("Starting application with uvicorn")
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)