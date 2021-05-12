from modules import app

@app.route('/')
@app.route('/hello1')
def hello1():
   return "Hola, mundo 1"