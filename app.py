# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api_teste.views import *
from api_teste.models import *
# add_occupation, delete_occupation, get_occupation, add_user, get_user, delete_user


@app.route('/')
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/cadastro'
    app.db = SQLAlchemy(app)

    return app


if __name__ == '__main__':
    app.run(debug=True)
