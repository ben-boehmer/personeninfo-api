from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_list_cities():
    response = client.get("/cities")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_city():
    response = client.get("/cities/berlin")
    assert response.status_code == 200 or response.status_code == 404
