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
        utils.validate_args(data, Users.schema)
        return utils.post(Users.db_name, data)

    @classmethod
    def patch(cls):
        data = request.get_json(silent=True)
        utils.validate_args(data, Users.schema)
        return utils.patch(Users.db_name, data)
