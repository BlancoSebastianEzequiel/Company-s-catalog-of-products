from server.model.base import Model


class HelpModule(Model):
    db_name = 'help_module'

    schema = {
        'title': str,
        'description': str
    }

    unique_values = {
        'title': True,
        'description': False
    }

    validation = {}

    def __init__(self, data, _id=None, unique_values=False):
        self.built_validator_schema()
        super().__init__(data, _id, unique_values=unique_values)

    @classmethod
    def built_validator_schema(cls):
        cls.validation = {
            'title': lambda title: True,
            'description': lambda description: True
        }
