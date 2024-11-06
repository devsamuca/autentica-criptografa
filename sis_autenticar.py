from flask import Flask

sis_autenticar = Flask(__name__)
sis_autenticar.secret_key = 'KAt8W-%8]SeRh5Y'

from rotas import *

if __name__ == '__main__':
    sis_autenticar.run(debug=True, host="192.168.0.200",port=80)
