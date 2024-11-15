import mysql.connector

def Conexao():
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Root",
            database="local"
        ) 
        if conexao.is_connected():
            return conexao
        else:
            return None
