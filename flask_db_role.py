# -*- coding: utf-8 -*-
from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'cadastro'
mysql = MySQL(app)


@app.route("/")
def teste():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM role''')

    name = cur.fetchall()
    return str(name)


@app.route("/addrole", methods=["POST"])
def add():  # Metodo
    import ipdb
    ipdb.set_trace()
    cur = mysql.connection.cursor()
    cur.execute('''SELECT MAX(id_role) FROM role''')
    maxid = cur.fetchone()
    cur.execute('''INSERT INTO role (id_role, role) VALUES (%s, %s)''', (maxid[0] + 1))
    mysql.connection.commit()
    return "Done"


if __name__ == '__main__':
    app.run(debug=True)
