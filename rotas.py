from flask import Flask, render_template, url_for, redirect, request, flash
from app import app
import hashlib
import mysql.connector
from Flask.autenticar.conexao import Conexao

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register", methods=['POST', 'GET'])
def cadastrar():
    
    if request.method == 'POST':
        
        nome = request.form.get('nome')    
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        senha_cripto = hashlib.sha256(senha.encode()).hexdigest()
        
        sql = "INSERT INTO USUARIOS(NOME,USUARIO,SENHA) VALUES(%s, %s, %s)"
        
        try:
            if nome == None:
                flash("O Nome não pode estar vazio")
                return redirect("/register")
            if usuario == None:
                flash("O Usuario não pode estar vazio")
                return redirect("/register")
            if len(senha) > 10:
                flash("Sua senha deve ter pelo menos 10 caracteres!")
                return redirect("/")
            
            cnx = Conexao()
            cursor = cnx.cursor()
            comando = (sql, (nome,usuario,senha_cripto))
            
            cursor.execute(comando)
            cnx.commit()
            return redirect("/register")    
        
        except mysql.connector.Error as Erro:
            flash(f"Erro ao conectar com o banco de dados {Erro}")
            return redirect("/register")
    else:
        return render_template("register.html")


@app.route("/welcome",  methods=['POST', 'GET'])
def autentica():
    
    if request.method == 'POST':
        
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        
        hash_senha = hashlib.sha256(senha.encode()).hexdigest()
        
        return render_template("welcome.html", usuario=usuario, senha=hash_senha)
    else:
        return redirect('/')


