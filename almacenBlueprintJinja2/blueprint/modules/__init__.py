from flask import Flask
from modules.product.views import product

app = Flask(__name__)
app.register_blueprint(product)
app.config['SQLALCHEMY_DATABASE_URI']

@app.template_filter('mydouble')
def mydouble_filter(n:int):
    return n * 2