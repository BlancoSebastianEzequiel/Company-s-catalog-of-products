from functools import wraps
from flask import current_app, g
from server.controller.utils import response
from http import HTTPStatus as http


def admin_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_app.config['SKIP_AUTH']:
            return func(*args, **kwargs)
        if g.type != 'admin':
            return response(data='Unauthorized', ok=False), http.UNAUTHORIZED
        return func(*args, **kwargs)
    return decorated_function
