from flask import Blueprint
from flask import request
from server.controller.company_data import CompanyDataController
from server.controller.utils import response
from server.decorators.login_required import login_required

COMPANY_DATA_BP = Blueprint(
    'company_data',
    __name__,
    url_prefix='/company_data'
)


@COMPANY_DATA_BP.route('/<_id>/', methods=['DELETE'])
@login_required
def delete_data(_id):
    res, status = CompanyDataController.delete(_id)
    return response(res['data'], res['ok']), status


@COMPANY_DATA_BP.route('/<_id>/', methods=['GET'])
@login_required
def get(_id):
    res, status = CompanyDataController.get(_id)
    return response(res['data'], res['ok']), status


@COMPANY_DATA_BP.route('/', methods=['GET'])
@login_required
def get_all():
    args = dict(request.args)
    for field in args:
        args[field] = args[field][0]
    res, status = CompanyDataController.get_all(args)
    return response(res['data'], res['ok']), status


@COMPANY_DATA_BP.route('/', methods=['PATCH'])
@login_required
def patch():
    res, status = CompanyDataController.patch(request.get_json(silent=True))
    return response(res['data'], res['ok']), status


@COMPANY_DATA_BP.route('/', methods=['POST'])
@login_required
def post():
    res, status = CompanyDataController.post(request.get_json(silent=True))
    return response(res['data'], res['ok']), status
