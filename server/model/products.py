from server.model.base import Model


class Products(Model):
    db_name = 'products'

    schema = {
        'code': str,
        'name': str,
        'description': str,
        'images': list,
        'size': str,  # (70 ml, 100 ml, 150 ml, 250 ml).
        'active_principle': str
    }

    unique_values = {
        'code': True,
        'name': False,
        'description': False,
        'images': False,
        'size': False,
        'active_principle': False,
    }

    def __init__(self, data, _id=None, unique_values=False):
        super().__init__(data, _id, unique_values=unique_values)
