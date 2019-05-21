from flask import Blueprint
from flask import request
from server.controller.active_principle import ActivePrincipleController
from server.controller.utils import response
from server.decorators.login_required import login_required

ACTIVE_PRINCIPLE_BP = Blueprint(
    'active_principle',
    __name__,
    url_prefix='/active_principle'
)


@ACTIVE_PRINCIPLE_BP.route('/<_id>/', methods=['DELETE'])
@login_required
def delete_user(_id):
    res, status = ActivePrincipleController.delete(_id)
    return response(res['data'], res['ok']), status


@ACTIVE_PRINCIPLE_BP.route('/<_id>/', methods=['GET'])
@login_required
def get(_id):
    res, status = ActivePrincipleController.get(_id)
    return response(res['data'], res['ok']), status


@ACTIVE_PRINCIPLE_BP.route('/', methods=['GET'])
@login_required
def get_all():
    args = dict(request.args)
    for field in args:
        args[field] = args[field][0]
    res, status = ActivePrincipleController.get_all(args)
    return response(res['data'], res['ok']), status


@ACTIVE_PRINCIPLE_BP.route('/', methods=['PATCH'])
@login_required
def patch():
    data = request.get_json(silent=True)
    res, status = ActivePrincipleController.patch(data)
    return response(res['data'], res['ok']), status


@ACTIVE_PRINCIPLE_BP.route('/', methods=['POST'])
@login_required
def post():
    data = request.get_json(silent=True)
    res, status = ActivePrincipleController.post(data)
    return response(res['data'], res['ok']), status
