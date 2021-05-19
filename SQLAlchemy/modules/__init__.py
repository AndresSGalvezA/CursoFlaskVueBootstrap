from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('configuration.DevelopmentConfig')
db = SQLAlchemy(app)

from modules.product.views import product
app.register_blueprint(product)
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