from flask import Flask

#Instancia a classe Flask
app = Flask(__name__)

#Arquivo de configuracao Flask
app.config.from_object('config')

#Apontamento do controller
from app.controllers import default
