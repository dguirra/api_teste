# -*- coding: utf-8 -*-
from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy
from views import *
# add_occupation, delete_occupation, get_occupation, add_user, get_user, delete_user

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/cadastro'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app


if __name__ == '__main__':
    app.run(debug=True)
