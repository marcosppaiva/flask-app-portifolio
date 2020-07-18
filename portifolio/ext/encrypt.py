from flask_bcrypt import Bcrypt

bc = Bcrypt()

def init_app(app):
    bc.init_app(app)