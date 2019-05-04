import server.controller.utils as utils
from server.controller.utils import response
from http import HTTPStatus as http
from flask import request
from server.model.users import Users


class UsersController:

    @classmethod
    def delete(cls, _id):
        try:
            user = Users.get(_id)
            _id = user.delete()
            return response(str(_id), True), http.OK
        except Exception as e:
            return response(f"Error deleting: {e}", False), http.BAD_REQUEST

    @classmethod
    def get(cls, _id):
        try:
            return response(Users.get(_id)._data, True), http.OK
        except Exception as e:
            return response(f"Error getting one: {e}", False), http.BAD_REQUEST

    @classmethod
    def get_all(cls):
        try:
            return response(Users.get_all(dict(request.args)), True), http.OK
        except Exception as e:
            return response(f"Error getting all: {e}", False), http.BAD_REQUEST

    @classmethod
    def post(cls):
        data = request.get_json(silent=True)
        try:
            _id = Users(data).post()
            return response(str(_id), True), http.OK
        except Exception as e:
            return utils.response(f"Error posting: {e}", False), http.BAD_REQUEST

    @classmethod
    def patch(cls):
        data = request.get_json(silent=True)
        try:
            _id = data.get('_id')
            data.pop('_id')
            _id = Users.get(_id).patch(data)
            return response(str(_id), True), http.OK
        except Exception as e:
            return utils.response(f"Error patching: {e}", False), http.BAD_REQUEST
