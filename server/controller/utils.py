from flask import jsonify


# pylint: disable=C0103
def response(message: str, ok: bool, **kwargs):
    """Arma una respuesta json generica"""
    return jsonify({'message': message, 'ok': ok, **kwargs})
