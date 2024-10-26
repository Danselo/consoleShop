import mysql.connector
import os
import pandas as pd

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
        cursor.close()
        db.close()
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
        cursor.close()
        database.close()
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
        cursor.close()
        database.close()
        return result





# MENU PARA ADMIN



def Listar_Personas():
    db = Connect_Database()
    cursor = db.cursor()
    query = """SELECT * FROM persona"""
    try:
        cursor.execute(query)
    except:
        result = False
    else:
        registros = cursor.fetchall()
        columnas = [desc[0] for desc in cursor.description] # Obtener los nombres de columna
        result = pd.DataFrame(registros,columns= columnas)
    finally:
        cursor.close()
        db.close()
        return result



def Buscar_Usuario_Correo(correo):
    db = Connect_Database()
    cursor = db.cursor()
    query = """SELECT usuario_id, correo FROM persona WHERE correo = %s """
    value = (correo,)
    try:
        cursor.execute(query,value)
    except:
        result = False
    else:
        registros = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        result = pd.DataFrame(registros, columns= columns)
    finally:
        cursor.close()
        db.close()
        return result


def Buscar_usario_id(id):
    db = Connect_Database()
    cursor = db.cursor()
    query = """SELECT usuario_id,correo FROM persona WHERE usuario_id = %s """
    value = (id,)
    try:
        cursor.execute(query, value)
    except:
        result = False
    else:
        registros = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        result = pd.DataFrame(registros, columns=columns)
    finally:
        cursor.close()
        db.close()
        return result


def Eliminar_Usuario(id):
    db = Connect_Database()
    cursor = db.cursor()
    query = """DELETE FROM persona WHERE usuario_id = %s"""
    value = (id,)

    usuario = Buscar_usario_id(id)
    #SI EL USUARIO NO SE ENCUENTRA PAILA
    if usuario.empty:
        return []
    else:
        try:
            cursor.execute(query,value)
        except:
            db.rollback()
            result = False
        else:
            result = True
            db.commit()
        finally:
            return result

