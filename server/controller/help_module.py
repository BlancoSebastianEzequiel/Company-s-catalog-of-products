from http import HTTPStatus as http
from server.model.help_module import HelpModule
from server.exceptions.status_exception import StatusException
from server.controller.abm_db_controller import ABMController


class HelpModuleController(ABMController):

    db = HelpModule
    name = 'help_module'

    @classmethod
    def post(cls, data):
        try:
            _id = HelpModule(data, unique_values=True).post()
            return {'data': str(_id), 'ok': True}, http.CREATED
        except StatusException as e:
            return {'data': f"Error posting: {e}", 'ok': False}, e.status
