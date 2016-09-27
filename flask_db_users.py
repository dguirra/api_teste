# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/cadastro'
db = SQLAlchemy(app)


class Occupation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    occupation = db.Column(db.String(100), unique=True, nullable=False)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(50))
    birth = db.Column(db.Date)
    id_occupation = db.Column(db.Integer, db.ForeignKey('occupation.id'))


@app.route('/user', methods=["POST"])
def add():
    data = request.json
    if isinstance(data, dict):  # Checa se é 'dict'
        user = User()
        user.name = data.get('name')
        user.last_name = data.get('last_name')
        user.birth = data.get('birth')
        _occupation = Occupation.query.filter_by(occupation=data.get('occupation')).one()
        user.id_occupation = _occupation.id
        db.session.add(user)

    elif isinstance(data, list):  # Checa se é 'list'
        for row in data:
            user = User()
            user.name = row.get('name')
            user.last_name = row.get('last_name')
            user.birth = row.get('birth')
            _occupation = Occupation.query.filter_by(occupation=row.get('occupation')).one()
            user.id_occupation = _occupation.id
            db.session.add(user)
    else:
        return jsonify({"Error": "Dados inseridos de forma incorreta"})
    db.session.commit()

    return jsonify({"name": user.name, "last_name": user.last_name,
                    "birth": user.birth, "occupation": user.occupation,
                    "occupation": _occupation.occupation, "id": user.id})


@app.route('/user/<id>')  # Por default é GET
def getuser(id):
    user = User.query.filter_by(id=id).first_or_404()
    return jsonify({"name": user.name, "last_name": user.last_name,
                    "birth": user.birth, "occupation": user.occupation,
                    "id": user.id})


@app.route('/user/<id>', methods=["DELETE"])
def delete(id):
    delete = User.query.filter_by(id=id).one()
    if delete != []:
        db.session.delete(delete)
        db.session.commit()
        return jsonify({"Status": "Success"})

    return jsonify({"Status": "Fail"})


if __name__ == '__main__':
    app.run(debug=True)
