import server.controller.utils as utils
from flask import request


class UsersController:

    db_name = "users"

    schema = {
        'first_name': str,
        'last_name': str,
        'mail': str,
        'password': str,
        'dni': str,
    }

    @classmethod
    def delete(cls, _id):
        return utils.delete(cls.db_name, _id)

    @classmethod
    def get(cls, _id):
        return utils.get(cls.db_name, _id)

    @classmethod
    def get_all(cls):
        return utils.get_all(cls.db_name, request.args)

    @classmethod
    def post(cls):
        data = request.get_json(silent=True)
        utils.validate_args(data, cls.schema)
        return utils.post(cls.db_name, data)

    @classmethod
    def patch(cls):
        data = request.get_json(silent=True)
        utils.validate_args(data, cls.schema)
        return utils.patch(cls.db_name, data)
