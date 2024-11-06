from flask import Flask

app = Flask(__name__)
app.secret_key = 'KAt8W-%8]SeRh5Y'

from rotas import *

if __name__ == '__main__':
    app.run(debug=True, host="192.168.0.200",port=80)
