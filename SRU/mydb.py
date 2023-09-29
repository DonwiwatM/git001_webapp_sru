import mysql.connector

dataBase = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '!T0878281390t')

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE donwiwat")

print("All done")