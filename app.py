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
    cur.execute('''SELECT * FROM pessoas''')
    rv = cur.fetchall()
    return str(rv)

@app.route("/addone/<string:insert>")
def add(insert):
    cur = mysql.connection.cursor()
    cur.execute('''INSERT INTO pessoas (id, nome) VALUES (%s, %s)''', (id[0] + 1, insert))
    mysql.connection.commit()
    return str (id, nome)
if __name__ == '__main__':
    app.run(debug=True)