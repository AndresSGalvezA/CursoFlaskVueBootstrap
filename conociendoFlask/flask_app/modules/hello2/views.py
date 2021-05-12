from modules import app

@app.route('/hello2')
def hello2():
   return "Hola, mundo 2"