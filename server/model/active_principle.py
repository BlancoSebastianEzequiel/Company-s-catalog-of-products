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

    validation = {}

    def __init__(self, data, _id=None, unique_values=False):
        self.built_validator_schema()
        super().__init__(data, _id, unique_values=unique_values)

    @classmethod
    def built_validator_schema(cls):
        cls.validation = {
            'code': lambda code: code.isdigit(),
            'name': lambda name: name.replace(" ", "").isalpha(),
            'description': lambda description: True
        }
