from http import HTTPStatus as http
from server.controller.utils import get_secret_password_from_hashed, send_email
from server.secrets import COMPANY_EMAIL, EMAIL_PASSWORD
from server.model.users import Users
from server.exceptions.status_exception import StatusException
from server.controller.abm_db_controller import ABMController


class UsersController(ABMController):

    db = Users
    name = 'user'

    @classmethod
    def post(cls, data):
        try:
            _id = Users(data, hash_pass=True, unique_values=True).post()
            return {'data': str(_id), 'ok': True}, http.CREATED
        except StatusException as e:
            return {'data': f"Error posting: {e}", 'ok': False}, e.status

    @classmethod
    def password_recovery(cls, email):
        res, status = cls.get_all({'email': email})
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
            send_email(COMPANY_EMAIL, EMAIL_PASSWORD, email, subject, message)
            msg = "the password was sent to your email"
            return {'data': msg, 'ok': True}, http.OK
        except Exception as e:
            msg = f"""
            Error sending email: {e}:\n
            Google is not allowing you to log in via smtplib because it has
            flagged this sort of login as "less secure", so what you have to
            do is go to this link while you're logged in to your google
            account, and allow the access:\n
            https://www.google.com/settings/security/lesssecureapps
            """
            return {'data': msg, 'ok': False}, http.INTERNAL_SERVER_ERROR

    @staticmethod
    def validate_contact_us_schema(info, schema):
        for field in schema:
            if field not in info:
                msg = f"Argument {field} missing"
                raise StatusException(msg, http.BAD_REQUEST)
            if not isinstance(info[field], schema[field]):
                msg = f"Argument {field} has invalid type"
                raise StatusException(msg, http.BAD_REQUEST)

    @classmethod
    def contact_us(cls, personal_info):
        contact_us_schema = {
            'email': str,
            'password': str,
            'subject': str,
            'message': str
        }
        try:
            cls.validate_contact_us_schema(personal_info, contact_us_schema)
        except StatusException as e:
            return {'data': e, 'ok': False}, e.status
        res, status = cls.get_all({'email': personal_info['email']})
        if not res['ok']:
            return {'data': res['data'], 'ok': False}, status
        if len(res['data']) != 1:
            msg = "email does not match to an existing user"
            return {'data': msg, 'ok': False}, http.BAD_REQUEST
        email = personal_info['email']
        password = personal_info['password']
        subject = personal_info['subject']
        message = personal_info['message']
        try:
            send_email(email, password, COMPANY_EMAIL, subject, message)
            msg = "the password was sent to your email"
            return {'data': msg, 'ok': True}, http.CREATED
        except Exception as e:
            msg = f"""
            Error sending email: {e}:\n
            Google is not allowing you to log in via smtplib because it has
            flagged this sort of login as "less secure", so what you have to
            do is go to this link while you're logged in to your google
            account, and allow the access:\n
            https://www.google.com/settings/security/lesssecureapps
            """
            return {'data': msg, 'ok': False}, http.INTERNAL_SERVER_ERROR
