from flask import Blueprint

hello2 = Blueprint('hello2', __name__)

@hello2.route('/hello2')
def sayHello():
   return "Hola, mundo 2 con Blueprint"