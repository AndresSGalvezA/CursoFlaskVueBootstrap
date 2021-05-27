from flask import Flask
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, logout_user, current_user
from functools import wraps
from werkzeug.utils import redirect

app = Flask(__name__)
app.config.from_object('configuration.DevelopmentConfig')
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.login_view = "fauth.login"
login_manager.init_app(app)

def rol_admin_need(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        if current_user.rol.value != 6:
            logout_user()
            return redirect(url_for('fauth.login'))
        
        return f(*args, **kwds)
    
    return wrapper

from modules.product.product import product
from modules.product.category import category
from modules.auth.views import auth
from modules.fauth.views import fauth

# Rest
from modules.rest_api.product_api import product_view
from modules.rest_api.category_api import category_view

app.register_blueprint(product)
app.register_blueprint(category)
# app.register_blueprint(auth)
app.register_blueprint(fauth)
db.create_all()

# SQLite
# sqlite:///database.db

# Postgres
# postgresql+psycopg2://user:password@ip:port/db_name

# MSSQL
# mssql+pyodbc://user:password@dsn_name

# Oracle
# oracle+cx_oracle://user:password@ip:port/db_name

@app.template_filter('mydouble')
def mydouble_filter(n:int):
    return n * 2