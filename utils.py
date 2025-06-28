from transformers import CLIPProcessor, CLIPModel
import torch
from PIL import Image
import numpy as np

def load_model():
    model = CLIPModel.from_pretrained("patrickjohncyh/fashion-clip")
    processor = CLIPProcessor.from_pretrained("patrickjohncyh/fashion-clip")
    return model, processor

def predict_image(model, processor, image: Image.Image):
    inputs = processor(text=["suit", "shirt", "tie", "jacket", "formalwear"], images=image, return_tensors="pt", padding=True)
    outputs = model(**inputs)
    logits_per_image = outputs.logits_per_image
    probs = logits_per_image.softmax(dim=1).detach().numpy()[0]

    labels = ["suit", "shirt", "tie", "jacket", "formalwear"]
    return {label: float(prob) for label, prob in zip(labels, probs)}