from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
from pathlib import Path
from Backend.text_utils import list_to_string, preprocessing

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model" / "text_model_pipeline.pkl"

pipeline = joblib.load(MODEL_PATH)

class TextInput(BaseModel):
    text: str

@app.post("/predict")
def predict(data: TextInput):
    proba = pipeline.predict_proba([data.text])[0]
    prob_fake = float(proba[0])
    prob_real = float(proba[1])

    prediction = 1 if prob_real >= 0.65 else 0

    return {
        "prob_fake": prob_fake,
        "prob_real": prob_real,
        "prediction": prediction
    }
