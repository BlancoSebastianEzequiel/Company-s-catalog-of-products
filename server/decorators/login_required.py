from functools import wraps
from flask import current_app, request
from server.controller.utils import response
from http import HTTPStatus as http
from server.controller.users import UsersController
from server.secrets import TOKEN_SERIALIZER


def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_app.config['SKIP_AUTH']:
            return func(*args, **kwargs)
        if 'HTTP_AUTHORIZATION' not in request.headers.environ:
            return response(data='Unauthorized', ok=False), http.UNAUTHORIZED
        token = request.headers.get('Authorization').split(' ')[1]
        data = TOKEN_SERIALIZER.loads(token)
        if '_id' not in data:
            return response(data='Unauthorized', ok=False), http.UNAUTHORIZED
        res, status = UsersController.get(data['_id'])
        if not res['ok']:
            return response(data=res['data'], ok=False), status
        return func(*args, **kwargs)
    return decorated_function
