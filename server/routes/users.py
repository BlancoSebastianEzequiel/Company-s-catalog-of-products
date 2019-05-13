from flask import Blueprint
from flask import request
from server.controller.users import UsersController
from server.controller.utils import response

USER_BP = Blueprint('users', __name__, url_prefix='/users')


@USER_BP.route('/<_id>/', methods=['DELETE'])
def delete_user(_id):
    res, status = UsersController.delete(_id)
    return response(res['data'], res['ok']), status


@USER_BP.route('/<_id>/', methods=['GET'])
def get(_id):
    res, status = UsersController.get(_id)
    return response(res['data'], res['ok']), status


@USER_BP.route('/', methods=['GET'])
def get_all():
    res, status = UsersController.get_all(dict(request.args))
    return response(res['data'], res['ok']), status


@USER_BP.route('/', methods=['PATCH'])
def patch():
    res, status = UsersController.patch()
    return response(res['data'], res['ok']), status


@USER_BP.route('/', methods=['POST'])
def post():
    res, status = UsersController.post()
    return response(res['data'], res['ok']), status
