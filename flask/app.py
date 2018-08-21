from flask import render_template

from middleware.cross_domain import allow_cross_domain
from action.login import login

from flask import Flask
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'zsw1'
app.config['MYSQL_DATABASE_PASSWORD'] = 'zsw123'
app.config['MYSQL_DATABASE_DB'] = 'zsw_db'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
mysql.init_app(app)


@app.route('/')
def hello_world():
    return render_template('hello.html', name="zzzzzzzzzzzzzzzzzz")


@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/login', methods=['POST', 'GET'])
@allow_cross_domain
def login_route():
    return login(mysql)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
    app.config['DEBUG'] = True

