from flask import Flask
from portifolio.ext import configuration
# from werkzeug import generate_password_hash, check_password_hash
# pip install flask-mysql (Mac/Linux)
# pip install Flask-MySQL (Windows)
# from flaskext.mysql import MySQL



def create_app():
    # mysql = MySQL()
    app = Flask(__name__)
    configuration.init_app(app)
    configuration.load_extensions(app)
    return app



# MySQL setup
# app.config['MYSQL_DATABASE_USER'] = 'appuser'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'app9872#'
# app.config['MYSQL_DATABASE_DB'] = 'appdb'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# mysql.init_app(app)


