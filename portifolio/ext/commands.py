import click
from portifolio.ext.database import db
from portifolio.models import User
from portifolio.ext.auth import create_user


def create_db():
    """Creates Database"""
    db.create_all()


def drop_db():
    db.drop_all()


def init_app(app):
    for command in [create_db, drop_db]:
        app.cli.add_command(app.cli.command()(command))


    @app.cli.command()
    @click.option('--username', '-u')
    @click.option('--password', '-p')
    def add_user(username, password):
        """Adds a new user to the database"""
        return create_user(username, password)