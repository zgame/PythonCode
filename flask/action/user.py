from flask import Flask, render_template, request, Response
import json


def logout(mysql):
    print("logout----")
    data = []
    return Response(json.dumps(data), mimetype='text/plain')



def login(mysql):
    error = None
    data = []
    print("dddddddddddddddddddddddddd")
    if request.method == 'POST':
        print("Post")
        print(request.body)
        received_json_data = json.loads(request.body)
        u1 = received_json_data.get('username')
        user = request.body.get('username')
        idx = request.form.get('password')

        print("get  user:", user)
        print("get  user:", u1)
        print("get  id:", idx)


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
