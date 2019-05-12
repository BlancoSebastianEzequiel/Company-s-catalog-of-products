from flask import jsonify


# pylint: disable=C0103
def response(data, ok, **kwargs):
    """Arma una respuesta json generica"""
    return jsonify({'data': data, 'ok': ok, **kwargs})
