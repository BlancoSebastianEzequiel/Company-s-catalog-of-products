from flask import Blueprint
from flask import request
from server.controller.help_module import HelpModuleController
from server.controller.utils import response
from server.decorators.login_required import login_required
from server.decorators.admin_required import admin_required

HELP_MODULE_BP = Blueprint(
    'help_module',
    __name__,
    url_prefix='/help_module'
)


@HELP_MODULE_BP.route('/<_id>/', methods=['DELETE'])
@login_required
@admin_required
def delete_help(_id):
    res, status = HelpModuleController.delete(_id)
    return response(res['data'], res['ok']), status


@HELP_MODULE_BP.route('/<_id>/', methods=['GET'])
@login_required
def get(_id):
    res, status = HelpModuleController.get(_id)
    return response(res['data'], res['ok']), status


@HELP_MODULE_BP.route('/', methods=['GET'])
@login_required
def get_all():
    args = dict(request.args)
    for field in args:
        args[field] = args[field][0]
    res, status = HelpModuleController.get_all(args)
    return response(res['data'], res['ok']), status


@HELP_MODULE_BP.route('/', methods=['PATCH'])
@login_required
@admin_required
def patch():
    res, status = HelpModuleController.patch(request.get_json(silent=True))
    return response(res['data'], res['ok']), status


@HELP_MODULE_BP.route('/', methods=['POST'])
@login_required
@admin_required
def post():
    res, status = HelpModuleController.post(request.get_json(silent=True))
    return response(res['data'], res['ok']), status
