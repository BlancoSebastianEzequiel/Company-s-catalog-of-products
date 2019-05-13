import bcrypt
from flask import jsonify


# pylint: disable=C0103
def response(data, ok, **kwargs):
    """Arma una respuesta json generica"""
    return jsonify({'data': data, 'ok': ok, **kwargs})


def get_hashed_password(secret_password):
    encoded_password = secret_password.encode('utf-8')
    return bcrypt.hashpw(encoded_password, bcrypt.gensalt(12)).decode()


def check_password(secret_password, hashed):
    return bcrypt.checkpw(secret_password.encode('utf-8'), hashed.encode())
