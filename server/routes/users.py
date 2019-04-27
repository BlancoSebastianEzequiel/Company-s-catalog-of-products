from flask import Blueprint
from server.controller.users import UsersController

USER_BP = Blueprint('users', __name__, url_prefix='/users')


@USER_BP.route('/<_id>/', methods=['DELETE'])
def delete_user(_id):
    return UsersController.delete(_id)


@USER_BP.route('/<_id>/', methods=['GET'])
def get(_id):
    return UsersController.get(_id)


@USER_BP.route('/', methods=['GET'])
def get_all():
    return UsersController.get_all()


@USER_BP.route('/', methods=['PATCH'])
def patch():
    return UsersController.patch()


@USER_BP.route('/', methods=['POST'])
def post():
    return UsersController.post()
