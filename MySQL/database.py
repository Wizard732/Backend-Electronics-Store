from multiprocessing import connection

import pymysql
from pip._internal.resolution.resolvelib import found_candidates

from MySQL.config import HOST,PASSWORD,USER,DATABASE
from handlers.models import products
from fastapi import HTTPException

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


def filter_db_max():
    connection = connect()
    if not connection:
        return {"error":"Не удалось подключится к БД"}

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM product WHERE price >= 500") # выводим данные с бд только если фильтр стоит выше 500
            rows = cursor.fetchall()
            return rows
    finally:
        if connection:
            connection.close() # закрываем бд только если было подключение


def filter_db_min():
    connection = connect()
    if not connection:
        return {"error":"Не удалось подключится к БД"}

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM product WHERE price < 500") # выводим данные с бд только если фильтр стоит выше 500
            rows = cursor.fetchall()
            return rows
    finally:
        if connection:
            connection.close() # закрываем бд только если было подключение


def add_product(item: products):
    connection = connect()
    if not connection:
        return {"error":"Не удалось подключится к БД"}

    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO product (title,category,brand,price,stock_quantity,is_available) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (item.title,item.category,item.brand,item.price,item.stock_quantity,item.is_available)

            cursor.execute(sql,values) # добавляем данные в бд
            connection.commit()
            return {"message": "Данные успешно записаны в БД"}
    except Exception as e:
        return {"error": f"Ошибка при добавлении данных {e}"}
    finally:
        if connection:
            connection.close()


def delete(id: int):
    connection = connect()
    if not connection:
        return {"error": "Не удалось подключится к БД"}

    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM product WHERE id = %s"
            cursor.execute(sql,(id,)) # удаляем из таблицы продукт айди с введеным пользователем айди

            connection.commit()

        return {"message": f"Данные с id - {id} успешно удалены"}

    except Exception as e:
        return {"error": f"Ошибка при удалении данных {e}"}
    finally:
        connection.close()


def category_db(category: str ):
    connection = connect()
    if not connection:
        return {"message": "Не удалось подключится к БД"}

    try:
        with connection.cursor() as cursor:
            sql = "SELECT brand FROM product WHERE category = %s"
            cursor.execute(sql,(category,)) # если введенные данные пользователя совпадают с данными category в таблицу выводим brand
            rows = cursor.fetchall()

            return {"message": f"Товар с категорией {category} - {rows}"}

    except Exception as e:
        return {"error": f"Категория с именем - {category} не найдена {e}."}
    finally:
        if connection:
            connection.close()


def update_db(id: int, new_stock: int):
    connection = connect()
    if not connection:
        return {"message": "Не удалось подключится к БД"}

    try:
        with connection.cursor() as cursor:
            sql = "UPDATE product SET stock_quantity = %s WHERE id = %s"
            cursor.execute(sql,(new_stock, id)) # обновляем в таблице продукт значение stock_quantity если id равно введенному id пользователя

            connection.commit()

            if cursor.rowcount == 0:
                return {"error": f"Товар с id - {id} не найден"}
            return {"message": f"Данные stock_quantity успешно обновлены на - {new_stock}!"}

    except Exception as e:
        return {"error": f"Данные не удалось обновить {e}"}
    finally:
        connection.close()
