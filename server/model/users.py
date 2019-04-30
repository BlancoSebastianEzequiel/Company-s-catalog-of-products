from server.libs.mongo import JSONEncoder


class Users:
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

    def __init__(self, reg: dict):
        self._data = reg.copy()

    def to_json(self):
        data = self._data.copy()
        return JSONEncoder().encode(data)
