# Sistema de Autenticação e Criptografia!

Esse projeo consiste em uma aplicação web desenvolvida utilizando o framework Flask da linguagem Python para realizar um cadastro, passando como parametros, seu nome, um nome de usuario, e uma senha que será criptografada antes de ser armazenada em um banco de dados MySql, a criptografia utilizada foi a SHA256, essa criptografia foi desenvolvida pela Agencia de Sergurança Nacional dos EUA. Após o cadastro o usuario ja pode efetuar o login utilizando seu nome de usuario e a sua senha. 

## 🚀 Começando

- Para clonar esse projeto para um repositorio em sua maquina local você deve primeiro [Instalar o Git](https://git-scm.com/downloads) 
- Em seguida você deverá abrir o terminal git e ir até o diretorio onde o repositorio será clonado.
- Após isso, execute o comando
    - git clone https://github.com/devsamuca/autentica-criptografa.git
- Agora o repositorio ja está em seu computador com todos os arquivos e dependencias nessarias.

### 📋 Pré-requisitos

Para rodar essa aplicação em sua maquina, serão necessarios:

- [Windows 10 ou Superior](https://www.microsoft.com/pt-br/software-download/windows10iso)
- [Python 3.12 ou Superior](https://www.python.org/downloads/)
- [MySql Server & Workbench](https://dev.mysql.com/downloads/workbench/)
- [Navegador de sua preferencia](https://rockcontent.com/br/blog/navegador/)

Bibliotecas Python necessarias:
    [flask](https://flask.palletsprojects.com/en/stable/)
    [hashlib](https://docs.python.org/3/library/hashlib.html)
    [mysql.connector](https://pypi.org/project/mysql-connector-python/)

### 🔧 Instalação

- Para rodar essa está aplicação primeiramente você deverá adicionar o python como variavel de ambiente.
- Em seguida abra o terminal git e execute os seguintes comandos:
    - pip install flask
    - pip install mysql-connector
- Após isso baixe o MySql Installer e o execute.
- Utilizando o MySql Installer instale o MySql Server e o MySql Workbench.
- Defina a senha do usuario root como "Root".
- Em seguida faça a importação do arquivo dump.sql para o seu servidor mysql.
- Feito tudo isso, abra o terminal git novamente e navegue até a pasta raiz do projeto.
- Com a pasta raiz aberta execute o seguinte comando
    - python main.py
- Feito isso o servidor já estará funcionando e você poderá acessa-lo digitando "localhost" em seu navegador

## ⚙️ Executando os testes

Esse sistema permite que você cadastre usuarios e realize o login com os dados de um usuario ja cadastrado.

Você pode cadastrar um usuario atraves da rota "localhost/register"
Para cadastrar um usuario digite o nome completo do mesmo, um nome de usuario e uma senha.

Através da rota "localhost/" você pode realizar o login utilizando os dados de um usuario ja cadastrado

Caso as informações estejam corretas a tela carregada exibirá as informações do usuario,
incluindo a senha após a mesma ser criptografada

## 🛠️ Construído com

Para desenvolver esse projeto, eu utilizei as seguintes liguagens e ferramentas.

* [Python](https://www.w3schools.com/python/default.asp) - Linguagem utilizada no Servidor.
* [MySql Connector](https://www.mysql.com/products/connector/) - Driver para estabelecer a conexão com o banco de dados.
* [HashLib](https://docs.python.org/3/library/hashlib.html) - Biblioteca para criptografar a senha.
* [Flask](https://flask.palletsprojects.com/en/stable/) - FrameWork Web para desenvolver a aplicação.
* [Html](https://www.w3schools.com/html/default.asp) - Linguagem para estruturar as paginas.
* [Css](https://www.w3schools.com/css/default.asp) - Linguagem para adicionar estilos nas paginas.
* [Java Script](https://www.w3schools.com/js/default.asp) - Linguagem para adicionar funcionalidade nas páginas.
* [Git](https://git-scm.com/downloads) - Software para controle de versão do sistema.
* [Visual Studio Code](https://code.visualstudio.com/) - Editor de texto para escrever os códigos.

## 📌 Versão

Observe as [tags neste repositório](https://github.com/devsamuca/sistema-autenticar/tags) para ver as versões desse sistema. 

## ✒️ Autor

Desenvolvido por Samuel Souza 🌹
