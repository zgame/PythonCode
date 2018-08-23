from flask import render_template

from middleware.cross_domain import allow_cross_domain
# from action.login import login
import action.user

from flask import Flask
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'zsw1'  # 用户名
app.config['MYSQL_DATABASE_PASSWORD'] = 'zsw123'
app.config['MYSQL_DATABASE_DB'] = 'by_statis_db'  # 数据库
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
mysql.init_app(app)


# @app.route('/')
# def hello_world():
#     return render_template('hello.html', name="zzzzzzzzzzzzzzzzzz")
#
#
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)
#
#
# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User %s' % username


# 用户登录
@app.route('/user/login', methods=['GET', 'POST', 'OPTIONS'])
@allow_cross_domain
def login_route():
    return action.user.login(mysql)


# 用户登出
@app.route('/user/logout', methods=['GET', 'POST', 'OPTIONS'])
@allow_cross_domain
def logout_route():
    return action.user.logout(mysql)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
    app.config['DEBUG'] = True
