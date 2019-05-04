from server.model.base import Model


class Users(Model):
    db_name = 'users'

    schema = {
        'first_name': str,
        'last_name': str,
        'user_name': str,
        'mail': str,
        'password': str,
        'dni': str,
        'type': str
    }
