import pymysql

def conectar():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="123",
        database="smartfinance",
        cursorclass=pymysql.cursors.DictCursor
    )