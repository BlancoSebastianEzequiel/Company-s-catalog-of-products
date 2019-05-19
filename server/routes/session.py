from flask import Blueprint
from flask import request
from server.controller.session import Session
from server.controller.utils import response

SESSION_BP = Blueprint('session', __name__, url_prefix='/session')


@SESSION_BP.route('/', methods=['POST'])
def post():
    data = request.get_json(silent=True)
    res, status = Session.create_session(data['email'], data['password'])
    return response(res['data'], res['ok']), status
