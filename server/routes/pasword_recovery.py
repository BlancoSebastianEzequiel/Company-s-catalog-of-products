from flask import Blueprint
from server.controller.users import UsersController
from server.controller.utils import response

PASSWORD_RECOVERY_BP = Blueprint(
    'password_recovery',
    __name__,
    url_prefix='/password_recovery'
)


@PASSWORD_RECOVERY_BP.route('/<email>/', methods=['GET'])
def get(email):
    res, status = UsersController.password_recovery(email)
    return response(res['data'], res['ok']), status
