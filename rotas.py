from flask import Flask, render_template, url_for, redirect, request, flash
from main import main
import hashlib
import mysql.connector
from conexao import Conexao

@main.route("/", methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        
        cnx = Conexao()
        cursor = cnx.cursor()
        
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        hash_senha = hashlib.sha256(senha.encode()).hexdigest()
    
        sql_consulta = "SELECT NOME,USUARIO, SENHA FROM USUARIOS WHERE USUARIO = %s"
        
        cursor.execute(sql_consulta, (usuario,))
        consulta = cursor.fetchall()
        
        if consulta == []:
            flash("Esse usuario não existe!")
            return redirect("/")
        
        linha = consulta[0]
        
        v_nome = linha[0]
        v_usuario = linha[1]
        v_senha = linha[2]
        
        if v_usuario == usuario and v_senha == hash_senha:
            return render_template("welcome.html", nome = v_nome, usuario = v_usuario, senha = v_senha) 
        else:
            flash("Senha invalida!")
            return redirect("/")
            
    else:
        return render_template("index.html")
    
@main.route("/register", methods=['POST', 'GET'])
def cadastrar():
    
    if request.method == 'POST':
        
        nome = request.form.get('nome')  
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        senha_cripto = hashlib.sha256(senha.encode()).hexdigest()
        
        cnx = Conexao()
        cursor = cnx.cursor()
        
        try:
            if len(nome) < 5:
                flash("O Nome muito curto!")
                return redirect("/register")
            
            if len(usuario) < 3:
                flash("Nome de usuario muito curto!")
                return redirect("/register")
            
            def verificar_usuarios():
                sql_pegar_usuarios = "SELECT USUARIO FROM USUARIOS"
                cursor.execute(sql_pegar_usuarios)
                
                usuarios_existentes = cursor.fetchall()
                usuarios_existentes = [item[0] for item in usuarios_existentes]
                
                for usuarios in usuarios_existentes:
                    if usuarios == usuario:
                        return "O usuarios inserido ja existe!"
                    
            verifica_usuarios = verificar_usuarios()
            if verifica_usuarios == "O usuarios inserido ja existe!":
                flash(verifica_usuarios)
                return render_template("register.html")
                
                
            if len(senha) < 4:
                flash("Sua senha deve ter pelo menos 10 caracteres!")
                return render_template("register.html")
            
            dados = nome, usuario, senha_cripto
            
            sql_cadastra_usuario = "INSERT INTO USUARIOS(NOME,USUARIO,SENHA) VALUES(%s, %s, %s)"
            cursor.execute(sql_cadastra_usuario, dados)
            cnx.commit()
            flash("Cadastrado com sucesso!")
            return redirect("/register")    
        
        except mysql.connector.Error as Erro:
            flash(f"{Erro}")
            return redirect("/register")
    else:
        return render_template("register.html")


