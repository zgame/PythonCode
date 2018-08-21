from flask import Flask, render_template, request, Response
import json


def login(mysql):
    error = None
    data = []
    if request.method == 'GET':
        user = request.args.get('user')
        idx = request.args.get('id')

        print("get  user:", user)
        print("get  id:", idx)

        data.append(user)
        data.append(idx)
        print("data:", data)

        cursor = mysql.connect().cursor()
        cursor.execute('SELECT * from student where true')
        data = cursor.fetchall()
        # data = cursor.fetchone()

        print("sql data:", data)
        # if data is None:
        #     return "Username or Password is wrong"
        # else:
        #     return data

    return Response(json.dumps(data), mimetype='text/plain')
    # return render_template('login.html', error=error, data=data)
