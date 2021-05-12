from flask import Flask
from modules.hello1.views import hello
from modules.hello2.views import hello2

app = Flask(__name__)
app.register_blueprint(hello)
app.register_blueprint(hello2)