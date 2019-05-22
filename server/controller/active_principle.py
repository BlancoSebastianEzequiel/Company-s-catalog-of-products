from http import HTTPStatus as http
from server.model.active_principle import ActivePrinciple
from server.exceptions.status_exception import StatusException
from server.controller.abm_db_controller import ABMController


class ActivePrincipleController(ABMController):

    db = ActivePrinciple
    name = 'active principle'

    @classmethod
    def post(cls, data):
        try:
            _id = ActivePrinciple(data, unique_values=True).post()
            return {'data': str(_id), 'ok': True}, http.CREATED
        except StatusException as e:
            return {'data': f"Error posting: {e}", 'ok': False}, e.status
