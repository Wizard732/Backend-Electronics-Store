import pymysql
from MySQL.config import HOST,PASSWORD,USER,DATABASE
from handlers.models import products

def connect():
    try:
        connection = pymysql.connect(
            host=HOST,
            password=PASSWORD, # Подключаемся к бд
            user=USER,
            database=DATABASE
        )
        return connection
    except Exception as e:
        print(f"Ошибка подключения к БД: {e}")


def read_db():
    connection = connect()
    if connection is None: # Если подключение не произошло выводим ошибку
        return {"error":"Не удалось подключится к БД"}

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM product")
            rows = cursor.fetchall()
            return  rows# выводим список
    finally:
        if connection:
            connection.close() # закрываем бд только если было подключение


