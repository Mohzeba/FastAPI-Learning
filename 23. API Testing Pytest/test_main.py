from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_add():
    response = client.get("/add?a=3&b=5")
    assert response.status_code == 200
    assert response.json() == {"result": 8}