from flask import Flask, url_for, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola, mundo con Flask'

@app.route('/test')
def hello_world2():
    return 'Una prueba'

@app.route('/saludar')
@app.route('/saludar/<hi>')
@app.route('/saludar/<hi>/<lang>')
def saludar(hi='', lang='es'):
    return 'Hola, ' + hi + ', ' + lang

@app.route('/primerHTML')
@app.route('/primerHTML/<name>')
def primerHTML(name='Andres'):
    return '''
        <html>
            <body>
                <h1> Hola con Flask</h1>
                <p>Hola, %s.</p>

                <ul>
                    <li>Cosa 1</li>
                    <li>Cosa 2</li>
                </ul>
            </body>
        </html>
    ''' %name

@app.route('/staticFile')
def staticFile():
   # return "<img src='/static/img/b11.png'>"
   return "<img src='" + url_for("static", filename = "img/b11.png") + "'>" # Tambien de esta manera

@app.route('/template')
@app.route('/template/<name>')
def template(name='Andres'):
   return render_template('view.html', vname = name)

# Si este archivo se ejecuta directamente con python app.py
if __name__ == '__main__':
    app.run()