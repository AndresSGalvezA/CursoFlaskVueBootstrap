from modules import app

app.config.from_object('configuration.ProductionConfig') # Y esta una opcion mas completa
# app.config.from_pyfile('config.py') # Esta es una opcion mejor
app.run() # debug=True entre los parentesis es una opcion
# app.config['debug'] = True # esta es otra
#app.debug = True # Y esta, otra