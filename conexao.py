import mysql.connector

conexao = mysql.connector.connect(
    host="192.168.0.200",
    user="samuca",
    password="8415",
    database="dbsamuca"
)

if conexao.is_connected():
    print(True)
