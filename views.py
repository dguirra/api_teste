# -*- coding: utf-8 -*-
from app import create_app
from flask import request, jsonify
from models import Occupation, User, db
from sqlalchemy import or_

app = create_app()


@app.route('/occupation', methods=["POST"])
def add_occupation():
    data = request.json
    if isinstance(data, dict):
        occupation = Occupation()
        occupation.description = data.get('description')
        db.session.add(occupation)

    elif isinstance(data, list):
        for row in data:
            occupation = Occupation()
            occupation.description = row.get('description')
            db.session.add(occupation)
    else:
        return jsonify({"Error": "Dados inseridos de forma incorreta"})
    db.session.commit()

    return jsonify({"Status": "Success"})


@app.route('/occupation/<params>')  # Por default é GET
def get_occupation(params):
    occupation = Occupation.query.filter(or_(Occupation.id == params,
                                             Occupation.description == params)).first_or_404()
    return jsonify({"description": occupation.description})


@app.route('/occupation/<id>', methods=["DELETE"])
def delete_occupation(id):
    delete = Occupation.query.filter_by(id=id).one()
    if delete != []:
        db.session.delete(delete)
        db.session.commit()
        return jsonify({"Status": "Success"})

    return jsonify({"Status": "Fail"})


# user
@app.route('/user', methods=["POST"])
def add_user():
    data = request.json
    if isinstance(data, dict):  # Checa se é 'dict'
        user = User()
        user.name = data.get('name')
        user.last_name = data.get('last_name')
        user.birth = data.get('birth')
        _occupation = Occupation.query.filter_by(description=data.get('occupation')).first()
        user.id_occupation = _occupation.id
        db.session.add(user)

    elif isinstance(data, list):  # Checa se é 'list'
        for row in data:
            user = User()
            user.name = row.get('name')
            user.last_name = row.get('last_name')
            user.birth = row.get('birth')
            _occupation = Occupation.query.filter_by(description=row.get('occupation')).first()
            user.id_occupation = _occupation.id
            db.session.add(user)
    else:
        return jsonify({"Error": "Dados inseridos de forma incorreta"})
    db.session.commit()

    return jsonify({"name": user.name, "last_name": user.last_name,
                    "birth": user.birth, "id_occupation": _occupation.description, "id": user.id})


@app.route('/user/<params>')  # Por default é GET
def get_user(params):
    query = User.query
    query = query.with_entities(User.name, User.last_name, User.birth,
                                Occupation.description, User.id)
    query = query.join(Occupation)
    query = query.filter(or_(User.name == params, User.last_name == params))
    user = query.all()
    user_dict = [data._asdict() for data in user]
    return jsonify(dict(user=user_dict)), 200


@app.route('/user/<id>', methods=["DELETE"])
def delete_user(id):
    delete = User.query.filter_by(id=id).one()
    if delete != []:
        db.session.delete(delete)
        db.session.commit()
        return jsonify({"Status": "Success"})

    return jsonify({"Status": "Fail"})
