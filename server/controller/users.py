from http import HTTPStatus as http
from server.controller.utils import get_secret_password_from_hashed, send_email
from server.model.users import Users
from server.exceptions.status_exception import StatusException


class UsersController:

    @classmethod
    def delete(cls, _id):
        try:
            user_data = Users.get(_id)
            if user_data is None:
                msg = "user does not exist"
                return {'data': msg, 'ok': False}, http.BAD_REQUEST
            _id = Users(user_data, _id=_id).delete()
            return {'data': str(_id), 'ok': True}, http.OK
        except StatusException as e:
            return {'data': f"Error deleting: {e}", 'ok': False}, e.status

    @classmethod
    def get(cls, _id):
        try:
            return {'data': Users.get(_id), 'ok': True}, http.OK
        except StatusException as e:
            return {'data': f"Error getting one: {e}", 'ok': False}, e.status

    @classmethod
    def get_all(cls, args):
        try:
            return {'data': Users.get_all(args), 'ok': True}, http.OK
        except StatusException as e:
            return {'data': f"Error getting all: {e}", 'ok': False}, e.status

    @classmethod
    def post(cls, data):
        try:
            _id = Users(data, hash_pass=True, unique_values=True).post()
            return {'data': str(_id), 'ok': True}, http.CREATED
        except StatusException as e:
            return {'data': f"Error posting: {e}", 'ok': False}, e.status

    @classmethod
    def patch(cls, data):
        try:
            _id = data.get('_id')
            data.pop('_id')
            user_data = Users.get(_id)
            if user_data is None:
                msg = "user does not exist"
                return {'data': msg, 'ok': False}, http.BAD_REQUEST
            _id = Users(user_data, _id=_id).patch(data)
            return {'data': str(_id), 'ok': True}, http.CREATED
        except StatusException as e:
            return {'data': f"Error patching: {e}", 'ok': False}, e.status

    @classmethod
    def password_recovery(cls, email):
        try:
            res, status = cls.get_all({'email': email})
        except StatusException as e:
            return {'data': f"Error getting one: {e}", 'ok': False}, e.status
        if not res['ok']:
            return {'data': res['data'], 'ok': False}, status
        if len(res['data']) != 1:
            msg = "email does not match to an existing user"
            return {'data': msg, 'ok': False}, http.BAD_REQUEST
        user_data = res['data'][0]
        hashed = user_data['password']
        secret = get_secret_password_from_hashed(hashed)
        subject = "ACPI: Password recovery"
        message = f"Your password is: {secret}"
        try:
            send_email(email, subject, message)
            msg = """
            the password was sent to your email:\n
            Google is not allowing you to log in via smtplib because it has 
            flagged this sort of login as "less secure", so what you have to 
            do is go to this link while you're logged in to your google 
            account, and allow the access:\n
            https://www.google.com/settings/security/lesssecureapps
            """
            return {'data': msg, 'ok': True}, http.OK
        except Exception as e:
            msg = f"Error sending email: {e}"
            return {'data': msg, 'ok': False}, http.INTERNAL_SERVER_ERROR
