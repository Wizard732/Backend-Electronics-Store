from fastapi import params
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_return_product():
    headers = {"admin": "admin"}
    result = client.get("/product", headers=headers)

    assert result.status_code == 200

def test_filter_max():
    params = {"price": 507}
    result = client.get("/filter/max_price", params=params)

    assert result.status_code == 200

def test_filter_min():
    params = {"price": 235}
    result = client.get("/filter/min_price", params=params)

    assert result.status_code == 200

def test_add_product():
    sql = {
  "title": "string",
  "category": "string",
  "brand": "string",
  "price": 2,
  "stock_quantity": 1,
  "is_available": True
}
    result = client.post("/add_product", json=sql)

    assert result.status_code == 200


def test_delete():
    params = {"id": 5}
    result = client.delete("/delete", params=params)

    assert result.status_code == 200


def test_category():
    params = {"category": "lelele"}
    result = client.get("/category", params=params)

    assert result.status_code == 200

def test_update():
    params = {"id": 1, "new_stock": 3}
    result = client.put("/update_product/(id)", params=params)

    assert result.status_code == 200