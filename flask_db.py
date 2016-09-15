from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'cadastro'
mysql = MySQL(app)


# Decorator
# https://www.codeschool.com/blog/2016/05/12/a-guide-to-python-decorators/
@app.route("/")
def teste():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM pessoas''')

    pessoa = cur.fetchall()
    return str(pessoa)


@app.route("/addone/<string:name>")
def add(name):  # Metodo
    cur = mysql.connection.cursor()
    cur.execute('''SELECT MAX(id_nome) FROM pessoas''')
    maxid = cur.fetchone()
    cur.execute('''INSERT INTO pessoas (id_nome, nome) VALUES (%s, %s)''', (maxid[0] + 1, name))
    mysql.connection.commit()
    return "Done"


if __name__ == '__main__':
    app.run(debug=True)
