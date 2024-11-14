from flask import Flask, render_template, url_for, redirect, request, flash, jsonify
from sis_autenticar import sis_autenticar
import hashlib
import mysql.connector
from conexao import Conexao

#Rota para home
@sis_autenticar.route("/", methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        
        cnx = Conexao()
        cursor = cnx.cursor()
        
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        hash_senha = hashlib.sha256(senha.encode()).hexdigest()
    
        #Valida se o usuario existe e se a senha esta correta
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
            return render_template("welcome.html", nome = v_nome, usuario = v_usuario) 
        else:
            flash("Senha invalida!")
            return redirect("/")
    else:
        return render_template("home.html")

#Rota para cadastrar
@sis_autenticar.route("/register", methods=['POST', 'GET'])
def cadastrar():
    
    if request.method == 'POST':
        
        nome = request.form.get('nome')  
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        senha_cripto = hashlib.sha256(senha.encode()).hexdigest()
        
        cnx = Conexao()
        cursor = cnx.cursor()
        
        try:
            # Verifica o tamanho do nome
            if len(nome) < 7:
                flash("O Nome muito curto!")
                return redirect("/register")
            
            # Verifica o tamanho do usuario
            if len(usuario) < 5:
                flash("Nome de usuario muito curto!")
                return redirect("/register")
            
            # Verifica se o Usuario ja existe
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
                
                
            # Verifica o tamanho da senha
            if len(senha) < 8:
                flash("Sua senha deve ter pelo menos 10 caracteres!")
                return render_template("register.html")
            
            #Dados para serem inseridos
            dados = nome, usuario, senha_cripto
            
            #Cadastrando o usuario
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


