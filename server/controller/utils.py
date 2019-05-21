import bcrypt
from flask import jsonify
from server.secrets import TOKEN_SERIALIZER


# pylint: disable=C0103
def response(data, ok, **kwargs):
    """Arma una respuesta json generica"""
    return jsonify({'data': data, 'ok': ok, **kwargs})


def get_hashed_password(secret_password):
    encoded_password = secret_password.encode('utf-8')
    return bcrypt.hashpw(encoded_password, bcrypt.gensalt(12)).decode()


def check_password(secret_password, hashed):
    return bcrypt.checkpw(secret_password.encode('utf-8'), hashed.encode())


def get_data_from_token(token):
    return TOKEN_SERIALIZER.loads(token)


def generate_token_from_data(data):
    return TOKEN_SERIALIZER.dumps(data).decode('utf-8')
