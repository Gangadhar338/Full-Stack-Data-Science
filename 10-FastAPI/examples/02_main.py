from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Data Science Course API", version="1.0.0")

class PredictionRequest(BaseModel):
    hours_studied: float = Field(ge=0, le=24)

class PredictionResponse(BaseModel):
    estimated_score: float

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    score = min(100.0, max(0.0, 40.0 + 2.5 * request.hours_studied))
    return PredictionResponse(estimated_score=round(score, 2))
