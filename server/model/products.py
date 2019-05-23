from server.model.base import Model
from server.controller.active_principle import ActivePrincipleController
from server.exceptions.status_exception import StatusException


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
        self.check_active_principle_existence(data)
        super().__init__(data, _id, unique_values=unique_values)

    @staticmethod
    def check_active_principle_existence(data):
        if 'active_principle' not in data:
            return
        code = data['active_principle']
        res, status = ActivePrincipleController.get_all({'code': code})
        if not res['ok']:
            raise StatusException(res['data'], status)
