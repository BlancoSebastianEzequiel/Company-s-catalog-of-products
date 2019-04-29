import server.controller.utils as utils
from flask import request
from server.model.users import Users


class UsersController:

    @classmethod
    def delete(cls, _id):
        return utils.delete(Users.db_name, _id)

    @classmethod
    def get(cls, _id):
        return utils.get(Users.db_name, _id)

    @classmethod
    def get_all(cls):
        return utils.get_all(Users.db_name, request.args)

    @classmethod
    def post(cls):
        data = request.get_json(silent=True)
        try:
            utils.validate_args(data, Users.schema)
            utils.validate_type(data, Users.schema)
            return utils.post(Users.db_name, data)
        except Exception as e:
            msg = f"Validation error: {e}"
            status = utils.http.BAD_REQUEST
            return utils.response(data=msg, ok=False), status

    @classmethod
    def patch(cls):
        data = request.get_json(silent=True)
        try:
            utils.validate_args(data, Users.schema)
            utils.validate_type(data, Users.schema)
            return utils.patch(Users.db_name, data)
        except Exception as e:
            msg = f"Validation error: {e}"
            status = utils.http.BAD_REQUEST
            return utils.response(data=msg, ok=False), status
