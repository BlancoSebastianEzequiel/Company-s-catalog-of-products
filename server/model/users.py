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
        'type': str
    }

    unique_values = {
        'first_name': False,
        'last_name': False,
        'user_name': True,
        'email': True,
        'password': False,
        'type': False
    }

    def __init__(self, data, _id=None, hash_pass=False, unique_values=False):
        if hash_pass and 'password' in data:
            data['password'] = get_hashed_password(data['password'])
        super().__init__(data, _id, unique_values=unique_values)
