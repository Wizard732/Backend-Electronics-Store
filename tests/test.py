from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_return_product():
    headers = {"admin": "admin"}
    result = client.get("/product", headers=headers)

    assert result.status_code == 200