from functools import wraps
from flask import make_response


def allow_cross_domain(fun):
    @wraps(fun)
    def wrapper_fun(*args, **kwargs):
        rst = make_response(fun(*args, **kwargs))
        rst.headers['Access-Control-Allow-Origin'] = 'http://localhost:9528'
        rst.headers['Access-Control-Allow-Methods'] = 'POST,PUT,GET,DELETE'
        # allow_headers = "Referer,Accept,Origin,User-Agent"
        rst.headers[
            'Access-Control-Allow-Headers'] = "Referer,Accept,Origin,User-Agent,x-custom,Origin, X-Requested-With, Content-Type, x-token"
        rst.headers['Access-Control-Allow-Credentials'] = "true"
        return rst

    return wrapper_fun
