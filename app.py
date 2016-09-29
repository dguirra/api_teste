 -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import or_


app = Flask(__name__)  # Perguntar!!!
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/cadastro'
db = SQLAlchemy(app)


class Occupation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), unique=True, nullable=False)