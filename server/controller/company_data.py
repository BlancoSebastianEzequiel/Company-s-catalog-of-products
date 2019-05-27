from http import HTTPStatus as http
from server.model.company_data import CompanyData
from server.exceptions.status_exception import StatusException
from server.controller.abm_db_controller import ABMController


class CompanyDataController(ABMController):

    db = CompanyData
    name = 'company_data'

    @classmethod
    def post(cls, data):
        try:
            _id = CompanyData(data, unique_values=True).post()
            return {'data': str(_id), 'ok': True}, http.CREATED
        except StatusException as e:
            return {'data': f"Error posting: {e}", 'ok': False}, e.status
