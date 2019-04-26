from flask import Blueprint
from flask_cors import cross_origin

from server.controller.utils import response
PING_BP = Blueprint('ping', __name__, url_prefix='/')


@PING_BP.route("/ping")
@cross_origin()
def ping():
    return response(message='pong', ok=True)
