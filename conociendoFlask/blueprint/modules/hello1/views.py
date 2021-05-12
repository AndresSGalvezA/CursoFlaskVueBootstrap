from flask import Blueprint

hello = Blueprint('hello', __name__)

@hello.route('/')
@hello.route('/hello1')
def hello1():
   return "Hola, mundo 1 con Blueprint"