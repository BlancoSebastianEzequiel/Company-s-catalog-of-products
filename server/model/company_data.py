from server.model.base import Model


class CompanyData(Model):
    db_name = 'company_data'

    schema = {
        'quantity_of_employees': str,
        'address': str,
        'capabilities': str,
        'mission': str,
        'vision': str,
        'values': str
    }

    unique_values = {
        'quantity_of_employees': False,
        'address': False,
        'capabilities': False,
        'mission': False,
        'vision': False,
        'values': False
    }

    validation = {}

    def __init__(self, data, _id=None, unique_values=False):
        self.built_validator_schema()
        super().__init__(data, _id, unique_values=unique_values)

    @classmethod
    def built_validator_schema(cls):
        cls.validation = {
            'quantity_of_employees': lambda q: q.isdigit(),
            'address': lambda a: True,
            'capabilities': lambda c: True,
            'mission': lambda m: True,
            'vision': lambda v: True,
            'values': lambda v: True,
        }
