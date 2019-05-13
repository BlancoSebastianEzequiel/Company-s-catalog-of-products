import jwt
from server.controller.users import UsersController
from server.controller.utils import check_password
from http import HTTPStatus as http


class Session:
    @classmethod
    def create_session(cls, email, secret_pass):
        res, status = UsersController.get_all({'mail': email})
        if not res['ok']:
            return res, status
        if len(res['data']) == 0:
            msg = "user does not exist"
            return {'data': msg, 'ok': False}, http.BAD_REQUEST
        user = res["data"][0]
        if check_password(secret_pass, user.__getitem__('password')):
            token = jwt.encode(
                user.get_data(),
                secret_pass,
                algorithm='HS256'
            )
            return {'data': token, 'ok': True}, http.OK
        else:
            return {'data': "Unauthorized", 'ok': False}, http.UNAUTHORIZED
