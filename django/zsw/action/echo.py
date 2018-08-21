import json

from django.http import HttpResponse


def echoz(request):
    error = None
    data = []
    if request.method == 'GET':
        user = request.GET.get('user')
        idx = request.GET.get('id')

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
