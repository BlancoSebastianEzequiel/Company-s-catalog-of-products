from server.model.base import Model


class ActivePrinciple(Model):
    db_name = 'active_principle'

    schema = {
        'code': str,  # unique value
        'name': str,
        'description': str,
    }

    unique_values = {
        'code': True,
        'name': False,
        'description': False
    }

    def __init__(self, data, _id=None, unique_values=False):
        super().__init__(data, _id, check_unique_values=unique_values)
