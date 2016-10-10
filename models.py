# -*- coding: utf-8 -*-
from app import db


class Occupation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), unique=True, nullable=False)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(50))
    birth = db.Column(db.Date)
    id_occupation = db.Column(db.Integer, db.ForeignKey('occupation.id'))
