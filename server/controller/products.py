from http import HTTPStatus as http
from server.model.products import Products
from server.exceptions.status_exception import StatusException
from server.controller.abm_db_controller import ABMController


class ProductsController(ABMController):

    db = Products
    name = 'product'

    @classmethod
    def post(cls, data):
        try:
            _id = Products(data, unique_values=True).post()
            return {'data': str(_id), 'ok': True}, http.CREATED
        except StatusException as e:
            return {'data': f"Error posting: {e}", 'ok': False}, e.status
