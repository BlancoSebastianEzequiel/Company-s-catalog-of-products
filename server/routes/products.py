from flask import Blueprint
from flask import request
from server.controller.products import ProductsController
from server.controller.utils import response
from server.decorators.login_required import login_required

PRODUCTS_BP = Blueprint('products', __name__, url_prefix='/products')


@PRODUCTS_BP.route('/<_id>/', methods=['DELETE'])
@login_required
def delete_product(_id):
    res, status = ProductsController.delete(_id)
    return response(res['data'], res['ok']), status


@PRODUCTS_BP.route('/<_id>/', methods=['GET'])
@login_required
def get(_id):
    res, status = ProductsController.get(_id)
    return response(res['data'], res['ok']), status


@PRODUCTS_BP.route('/', methods=['GET'])
@login_required
def get_all():
    args = dict(request.args)
    for field in args:
        args[field] = args[field][0]
    res, status = ProductsController.get_all(args)
    return response(res['data'], res['ok']), status


@PRODUCTS_BP.route('/', methods=['PATCH'])
@login_required
def patch():
    res, status = ProductsController.patch(request.get_json(silent=True))
    return response(res['data'], res['ok']), status


@PRODUCTS_BP.route('/', methods=['POST'])
@login_required
def post():
    res, status = ProductsController.post(request.get_json(silent=True))
    return response(res['data'], res['ok']), status
