from server.model.base import Model
from server.controller.utils import get_hashed_password


class Users(Model):
    db_name = 'users'

    schema = {
        'first_name': str,
        'last_name': str,
        'user_name': str,  # unique value
        'email': str,  # unique value
        'password': str,
        'dni': str,  # unique value
        'type': str
    }

    unique_values = {
        'first_name': False,
        'last_name': False,
        'user_name': True,
        'email': True,
        'password': False,
        'dni': True,
        'type': False
    }

    def __init__(self, data, _id=None, hash_pass=False, unique_values=False):
        if hash_pass:
            self.validate_key_in_schema('password')
            data['password'] = get_hashed_password(data['password'])
        super().__init__(data, _id, check_unique_values=unique_values)
