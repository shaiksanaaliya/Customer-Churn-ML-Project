from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_predict_missing_data():
    response = client.post("/predict", json={"data": {}})
    assert response.status_code == 200
    assert "error" in response.json() or "prediction" in response.json()


def test_predict_invalid_request():
    response = client.post("/predict", json={})
    assert response.status_code == 422
