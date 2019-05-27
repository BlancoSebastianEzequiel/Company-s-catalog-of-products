from http import HTTPStatus as http
from server.model.base import Model
from typing import Type
from server.exceptions.status_exception import StatusException


class ABMController:

    db: Type[Model]
    name = ''

    @classmethod
    def delete(cls, _id):
        try:
            db_data = cls.db.get(_id)
            if db_data is None:
                msg = f"{cls.name} does not exist"
                return {'data': msg, 'ok': False}, http.BAD_REQUEST
            _id = cls.db(db_data, _id=_id).delete()
            return {'data': str(_id), 'ok': True}, http.OK
        except StatusException as e:
            return {'data': f"Error deleting: {e}", 'ok': False}, e.status

    @classmethod
    def get(cls, _id):
        try:
            return {'data': cls.db.get(_id), 'ok': True}, http.OK
        except StatusException as e:
            return {'data': f"Error getting one: {e}", 'ok': False}, e.status

    @classmethod
    def get_all(cls, args):
        try:
            return {'data': cls.db.get_all(args), 'ok': True}, http.OK
        except StatusException as e:
            return {'data': f"Error getting all: {e}", 'ok': False}, e.status

    @classmethod
    def patch(cls, data):
        try:
            _id = data.get('_id')
            data.pop('_id')
            db_data = cls.db.get(_id)
            if db_data is None:
                msg = f"{cls.name} does not exist"
                return {'data': msg, 'ok': False}, http.BAD_REQUEST
            _id = cls.db(db_data, _id=_id).patch(data)
            return {'data': str(_id), 'ok': True}, http.CREATED
        except StatusException as e:
            return {'data': f"Error patching: {e}", 'ok': False}, e.status

    @classmethod
    def is_empty(cls):
        return cls.db.is_empty()
