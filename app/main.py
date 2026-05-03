from fastapi import FastAPI,Depends
import pymysql
from MySQL.config import HOST,PASSWORD, USER, DATABASE
from MySQL.database import connect, read_db
from handlers.admin import verify_admin
from handlers.models import products

app = FastAPI()

def connect_db():
    return connect()

@app.get("/product")
def product(admin: str = Depends(verify_admin)):
    return read_db()

