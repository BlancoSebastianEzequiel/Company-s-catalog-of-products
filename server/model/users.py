from server.model.base import Model
from server.controller.utils import get_hashed_password


class Users(Model):
    db_name = 'users'

    schema = {
        'first_name': str,
        'last_name': str,
        'user_name': str,
        'email': str,
        'password': str,
        'dni': str,
        'type': str
    }

    def __init__(self, data: dict, _id=None, hash_pass=False):
        if hash_pass:
            self.validate_key_in_schema('password')
            data['password'] = get_hashed_password(data['password'])
        super().__init__(data, _id)
