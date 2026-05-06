from fastapi import FastAPI,Depends, HTTPException
import pymysql
from MySQL.config import HOST,PASSWORD, USER, DATABASE
from MySQL.database import connect, read_db, filter_db_max, add_product, filter_db_min, delete, category_db, update_db
from handlers.admin import verify_admin
from handlers.models import products

app = FastAPI()

def connect_db():
    return connect()

@app.get("/product")
def product(admin: str = Depends(verify_admin)):
    return read_db()

@app.get("/filter/max_price")
def filter(price: float):
    return filter_db_max()

@app.get("/filter/min_price")
def filter(price: float):
    return filter_db_min()

@app.post("/add_product")
def add_to_db(item: products):
    return add_product(item)

@app.delete("/delete")
def delete_db(id: int):
    return delete(id)

@app.get("/category")
def category(category: str):
    return category_db(category)

@app.put("/update_product/(id)")
def update(id: int, new_stock: int):
    return update_db(id, new_stock)