from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_list_personen():
    response = client.get("/personen")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_person():
    response = client.get("/personen/benjamin")
    assert response.status_code == 200 or response.status_code == 404
