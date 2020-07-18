from portifolio.ext.database import db
from sqlalchemy_serializer import SerializerMixin


class User(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(140))
    password = db.Column(db.String(512))



class Relatorios(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    painel_name = db.Column(db.String(512))
    link = db.Column(db.Text)