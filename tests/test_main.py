from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_get_item():
    response = client.get("/items/5")
    assert response.status_code == 200
    assert response.json()["item_id"] == 5
