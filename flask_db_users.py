# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import or_
from flask_db_occupation import Occupation  # Importando a class Occupation


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/cadastro'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(50))
    birth = db.Column(db.Date)
    id_occupation = db.Column(db.Integer, db.ForeignKey('occupation.id'))


@app.route('/user', methods=["POST"])
def add_user():
    data = request.json  # 'data' recebendo parametros em JSON
    if isinstance(data, dict):  # Checa se é 'dict'
        user = User()
        user.name = data.get('name')  # O "('name')" é o parametro usado pelo JSON
        user.last_name = data.get('last_name')
        user.birth = data.get('birth')
        _occupation = Occupation.query.filter_by(description=data.get('occupation')).one()
        user.id_occupation = _occupation.id
        db.session.add(user)

    elif isinstance(data, list):  # Checa se é 'list'
        for row in data:  # O for é um laço para armazenar (no caso em 'data') os dados da lista
            user = User()
            user.name = row.get('name')
            user.last_name = row.get('last_name')
            user.birth = row.get('birth')
            _occupation = Occupation.query.filter_by(description=row.get('occupation')).one()
            user.id_occupation = _occupation.id
            db.session.add(user)
    else:
        return jsonify({"Error": "Dados inseridos de forma incorreta"})
    db.session.commit()

    return jsonify({"name": user.name, "last_name": user.last_name,
                    "birth": user.birth, "id_occupation": _occupation.occupation,
                    "id": user.id})


@app.route('/user/<params>')  # Por default é GET
def get_user(params):
    user = User.query.filter(or_(User.id == params,
                             User.name == params)).all()
    x = []
    if not user:
        return jsonify({"Status": "Fail", "mensagem": "A busca na retornou nenhum resultado"})
    for row in user:
        x.append({"name": row.name, "last_name": row.last_name,
                  "birth": row.birth, "occupation": row.id_occupation,
                  "id": row.id})
    return jsonify(x)


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
