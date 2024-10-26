from select import error

import mysql.connector
import os

from mysql.connector import connect

DATABASE_NAME = os.environ["DB_DATABASE"]
DATABASE_USERNAME = os.environ["DB_USERNAME"]
DATABASE_PASSWORD = os.environ["DB_PASSWORD"]
DATABASE_HOST= os.environ["DB_HOST"]

def ClearConsole():
    print("\n" * 100)

def Connect_Database():
    try:
        database = mysql.connector.connect(
            host = DATABASE_HOST,
            username = DATABASE_USERNAME,
            password = DATABASE_PASSWORD,
            database = DATABASE_NAME
        )
    except:
        print("Error al conectar a la base de datos")
    else:
        return database


def Registrar_Persona(correo,username,contraseña):
    db = Connect_Database()
    cursor = db.cursor()
    query = """INSERT INTO persona (correo,usuario,contraseña) VALUES (%s,%s,%s)"""
    value = (correo,username,contraseña)
    try:
        cursor.execute(query,value)
    except:
        db.rollback()
        result = False
    else:
        db.commit()
        result = True

    finally:
        return result


def Validar_Existencia_Correo(correo):
    database = Connect_Database()
    cursor = database.cursor()
    query = """SELECT correo FROM persona WHERE correo = %s """
    value = (correo,)
    try:
        cursor.execute(query,value)
    except:
        result = False
    else:
        result = ()
        for data in cursor:
            result = data
    finally:
        return result


def Login(correo,password):
    database = Connect_Database()
    cursor = database.cursor()
    query = """SELECT correo,contraseña FROM persona WHERE correo = %s AND contraseña = %s """
    value = (correo,password)
    try:
        cursor.execute(query,value)
    except:
        result = False
    else:
        result = ()
        for data in cursor:
            result = data
    finally:
        return result


