import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = ''
)

#Preparar el cursor
cursorObject = database.cursor()

#Crear database
cursorObject.execute("CREATE DATABASE gaspar")

print("Base de datos creada")
