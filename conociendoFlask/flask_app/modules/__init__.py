from flask import Flask
app = Flask(__name__)

# Importar vistas
import modules.hello1.views
import modules.hello2.views