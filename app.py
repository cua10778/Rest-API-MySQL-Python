import pytest

from flask_mysqldb import MySQL
from flask import Flask, render_template, request
import yaml

app = Flask(__name__)
mysql = MySQL(app)

db = yaml.safe_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == "POST":
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)",(name, email))
        mysql.connection.commit()
        cur.close()
        return 'Successfully added'
    return render_template('index.html')

@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    ShowValue = cur.execute("SELECT * FROM users")
    if ShowValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html', userDetails=userDetails)

if __name__ == '__main__':
    app.run(debug=True)