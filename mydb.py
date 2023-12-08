import mysql.connector 

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'MuMu321'
)

# cursor object 
cursorObject = dataBase.cursor()

# create a database

cursorObject.execute("CREATE DATABASE db2")

print("Database created")