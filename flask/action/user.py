from flask import Flask, render_template, request, Response
import json


def logout(mysql):
    print("logout----")
    data = []
    return Response(json.dumps(data), mimetype='text/plain')


def login(mysql):
    error = None
    data = []
    user = ''
    pwd = ''
    if request.method == 'OPTIONS':
        return Response("", mimetype='text/plain')

    if request.method == 'POST':
        received_json_data = json.loads(request.data)
        user = received_json_data.get('username')
        pwd = received_json_data.get('password')

    if request.method == 'GET':
        user = request.args.get('user')
        pwd = request.args.get('id')

    cursor = mysql.connect().cursor()
    cursor.execute("SELECT pwd FROM user where name = '" + user + "'")
    data = cursor.fetchall()

    sql_pwd = data[0][0]
    if sql_pwd == pwd:
        return "Username or Password is wrong"
    else:
        return data

    return Response(json.dumps(data), mimetype='text/plain')
    # return render_template('login.html', error=error, data=data)
