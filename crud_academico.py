import mysql.connector
from mysql.connector import Error

class crud:
    def __init__(self):
        try:
            print("Conectando a la base de datos...")
            self.conexion = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='db_academica',
                port=3306
            )
            if self.conexion.is_connected():
                print("Conexion exitosa a la base de datos")
            else:
                print("Error al conectar a la base de datos")
        except Error as e:
            print("Error de conexión:", e)
        
    def consultar(self, sql, valores=None):
        cursor = self.conexion.cursor(dictionary=True)
        if valores:
            cursor.execute(sql, valores)
        else:
            cursor.execute(sql)
        return cursor.fetchall()
    
    def ejecutar(self, sql, datos):
        try:
            cursor = self.conexion.cursor()
            cursor.execute(sql, datos)
            self.conexion.commit()
            return "ok"
        except Error as e:
            return str(e)
