import json

from django.http import HttpResponse
from mysql import get_sql_data

def login(request):
    error = None
    data = []
    if request.method == 'GET':
        user = request.GET.get('username')
        idx = request.GET.get('password')

        print("get  user:", user)
        print("get  id:", idx)

        data.append(user)
        data.append(idx)
        print("data:", data)
        #     if valid_login(request.form['username'],
        #                    request.form['password']):
        #         return log_the_user_in(request.form['username'])
        #     else:
        #         error = 'Invalid username/password'
        return HttpResponse(json.dumps(data), content_type="text/plain")

    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        user = received_json_data.get('username')
        idx = received_json_data.get('password', '')

        sql = "SELECT pwd FROM user where name = '" + user + "'"
        ppwd = get_sql_data(sql)
        print("get  user:", user)
        print("get  id:", idx)
        print("sql ppwd", ppwd)

        data.append(user)
        data.append(idx)
        print("data:", data)
        #     if valid_login(request.form['username'],
        #                    request.form['password']):
        #         return log_the_user_in(request.form['username'])
        #     else:
        #         error = 'Invalid username/password'
        return HttpResponse(json.dumps(data), content_type="text/plain")
