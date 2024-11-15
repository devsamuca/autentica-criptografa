from flask import Flask

main = Flask(__name__)
main.secret_key = 'KAt8W-%8]SeRh5Y'

from rotas import *

if __name__ == '__main__':
    main.run(debug=True, host="localhost", port=80)
