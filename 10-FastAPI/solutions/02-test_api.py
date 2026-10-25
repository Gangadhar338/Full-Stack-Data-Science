# Install: python -m pip install fastapi httpx
from fastapi.testclient import TestClient
from examples_02_main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_predict():
    response = client.post("/predict", json={"hours_studied": 4})
    assert response.status_code == 200
    assert response.json()["estimated_score"] == 50.0

def test_invalid_input():
    response = client.post("/predict", json={"hours_studied": 30})
    assert response.status_code == 422
