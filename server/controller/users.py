from http import HTTPStatus as http
from server.model.users import Users
from server.exceptions.status_exception import StatusException


class UsersController:

    @classmethod
    def delete(cls, _id):
        try:
            user = Users.get(_id)
            _id = user.delete()
            return {'data': str(_id), 'ok': True}, http.OK
        except StatusException as e:
            return {'data': f"Error deleting: {e}", 'ok': False}, e.status

    @classmethod
    def get(cls, _id):
        try:
            return {'data': Users.get(_id).get_data(), 'ok': True}, http.OK
        except StatusException as e:
            return {'data': f"Error getting one: {e}", 'ok': False}, e.status

    @classmethod
    def get_all(cls, args):
        try:
            return {'data': Users.get_all(args), 'ok': True}, http.OK
        except StatusException as e:
            return {'data': f"Error getting all: {e}", 'ok': False}, e.status

    @classmethod
    def post(cls, data):
        try:
            _id = Users(data, hash_pass=True).post()
            return {'data': str(_id), 'ok': True}, http.CREATED
        except StatusException as e:
            return {'data': f"Error posting: {e}", 'ok': False}, e.status

    @classmethod
    def patch(cls, data):
        try:
            _id = data.get('_id')
            data.pop('_id')
            _id = Users.get(_id).patch(data)
            return {'data': str(_id), 'ok': True}, http.CREATED
        except StatusException as e:
            return {'data': f"Error patching: {e}", 'ok': False}, e.status
