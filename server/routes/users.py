from flask import Blueprint
from flask import request
from server.controller.users import UsersController
from server.controller.utils import response
from server.decorators.login_required import login_required

USER_BP = Blueprint('users', __name__, url_prefix='/users')


@USER_BP.route('/<_id>/', methods=['DELETE'])
@login_required
def delete_user(_id):
    res, status = UsersController.delete(_id)
    return response(res['data'], res['ok']), status


@USER_BP.route('/<_id>/', methods=['GET'])
@login_required
def get(_id):
    res, status = UsersController.get(_id)
    return response(res['data'], res['ok']), status


@USER_BP.route('/', methods=['GET'])
@login_required
def get_all():
    res, status = UsersController.get_all(dict(request.args))
    return response(res['data'], res['ok']), status


@USER_BP.route('/', methods=['PATCH'])
@login_required
def patch():
    res, status = UsersController.patch(request.get_json(silent=True))
    return response(res['data'], res['ok']), status


@USER_BP.route('/', methods=['POST'])
def post():
    res, status = UsersController.post(request.get_json(silent=True))
    return response(res['data'], res['ok']), status
