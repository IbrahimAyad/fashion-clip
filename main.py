from fastapi import FastAPI, UploadFile, File
from utils import load_model, predict_image
from PIL import Image
import io

app = FastAPI()
model, processor = load_model()

@app.get("/")
def read_root():
    return {"message": "FashionCLIP API is running"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")
    predictions = predict_image(model, processor, image)
    return {"predictions": predictions}