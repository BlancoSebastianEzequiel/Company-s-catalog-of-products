from flask import Blueprint, request
from server.controller.users import UsersController
from server.controller.utils import response
from server.decorators.login_required import login_required

CONTACT_US_BP = Blueprint(
    'contact_us',
    __name__,
    url_prefix='/contact_us'
)


@CONTACT_US_BP.route('/', methods=['POST'])
@login_required
def post():
    res, status = UsersController.contact_us(request.get_json(silent=True))
    return response(res['data'], res['ok']), status
