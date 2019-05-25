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

    validation = {}

    def __init__(self, data, _id=None, hash_pass=False, unique_values=False):
        self.built_validator_schema()
        if hash_pass and 'password' in data:
            data['password'] = get_hashed_password(data['password'])
        super().__init__(data, _id, unique_values=unique_values)

    @classmethod
    def built_validator_schema(cls):
        cls.validation = {
            'first_name': lambda name: name.replace(" ", "").isalpha(),
            'last_name': lambda name: name.replace(" ", "").isalpha(),
            'user_name': lambda user_name: True,
            'email': lambda email: cls.validate_email_format(email),
            'password': lambda user_name: True,
            'type': lambda user_type: cls.validate_type_format(user_type)
        }

    @staticmethod
    def validate_email_format(email):
        from email.utils import parseaddr
        if '@' not in email:
            return False
        parse = parseaddr(email)
        if ('', '') == parse:
            return False
        return True

    @staticmethod
    def validate_type_format(user_type):
        return True if user_type in ['client', 'admin'] else False

    @staticmethod
    def hash_new_password(data):
        if 'password' not in data:
            return data
        data['password'] = get_hashed_password(data['password'])
        return data

    def patch(self, data):
        data = self.hash_new_password(data)
        return super().patch(data)
