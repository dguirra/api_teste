# -*- coding: utf-8 -*-
from flask import Flask, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'cadastro'
mysql = MySQL(app)


@app.route("/")
def teste():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM users''')

    name = cur.fetchall()
    return str(name)


@app.route("/addusers", methods=["POST"])
def add():
    import ipdb
    ipdb.set_trace()
    cur = mysql.connection.cursor()
    cur.execute('''SELECT MAX(id_user) FROM users''')
    maxid = cur.fetchone()
    cur.execute(""" INSERT INTO users (id_user, name, last_name,
                                       birth, occupation, id_role)
                    VALUES (%s, %s, %s, %s, %s, %s)""", [(maxid[0] + 1)])
    mysql.connection.commit()
    return "Done"


@app.route('/getall')
def getall():
    import ipdb
    ipdb.set_trace()
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM users''')
    returnvals = cur.fetchall()

    printthis = ""
    for i in returnvals:
        printthis += i + "<br>"

    return printthis


if __name__ == '__main__':
    app.run(debug=True)
