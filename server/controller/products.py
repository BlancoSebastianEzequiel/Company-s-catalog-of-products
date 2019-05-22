from http import HTTPStatus as http
from server.model.products import Products
from server.exceptions.status_exception import StatusException


class ProductsController:

    @classmethod
    def delete(cls, _id):
        try:
            products_data = Products.get(_id)
            if products_data is None:
                msg = "user does not exist"
                return {'data': msg, 'ok': False}, http.BAD_REQUEST
            _id = Products(products_data, _id=_id).delete()
            return {'data': str(_id), 'ok': True}, http.OK
        except StatusException as e:
            return {'data': f"Error deleting: {e}", 'ok': False}, e.status

    @classmethod
    def get(cls, _id):
        try:
            return {'data': Products.get(_id), 'ok': True}, http.OK
        except StatusException as e:
            return {'data': f"Error getting one: {e}", 'ok': False}, e.status

    @classmethod
    def get_all(cls, args):
        try:
            return {'data': Products.get_all(args), 'ok': True}, http.OK
        except StatusException as e:
            return {'data': f"Error getting all: {e}", 'ok': False}, e.status

    @classmethod
    def post(cls, data):
        try:
            _id = Products(data, unique_values=True).post()
            return {'data': str(_id), 'ok': True}, http.CREATED
        except StatusException as e:
            return {'data': f"Error posting: {e}", 'ok': False}, e.status

    @classmethod
    def patch(cls, data):
        try:
            _id = data.get('_id')
            data.pop('_id')
            products_data = Products.get(_id)
            if products_data is None:
                msg = "user does not exist"
                return {'data': msg, 'ok': False}, http.BAD_REQUEST
            _id = Products(products_data, _id=_id).patch(data)
            return {'data': str(_id), 'ok': True}, http.CREATED
        except StatusException as e:
            return {'data': f"Error patching: {e}", 'ok': False}, e.status
