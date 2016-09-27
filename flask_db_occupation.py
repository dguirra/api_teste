# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import or_


app = Flask(__name__)  # Perguntar!!!
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/cadastro'
db = SQLAlchemy(app)


class Occupation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), unique=True, nullable=False)


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
def delete(id):
    delete = Occupation.query.filter_by(id=id).one()
    if delete != []:
        db.session.delete(delete)
        db.session.commit()
        return jsonify({"Status": "Success"})

    return jsonify({"Status": "Fail"})


if __name__ == '__main__':
    app.run(debug=True)
