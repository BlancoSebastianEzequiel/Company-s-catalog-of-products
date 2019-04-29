from flask import jsonify
from http import HTTPStatus as http
from server.libs.mongo import MONGO
from server.model.users import Users
from bson import ObjectId


# pylint: disable=C0103
def response(data, ok, **kwargs):
    """Arma una respuesta json generica"""
    return jsonify({'data': data, 'ok': ok, **kwargs})


def db_result_to_json(result):
    return [Users(instance).to_json() for instance in result]


def delete(db_name, _id):
    collection = MONGO.db[db_name]
    try:
        result = collection.delete_one({"_id": ObjectId(_id)})
        if not result.deleted_count and result.acknowledged:
            msg = f"Error deleting"
            return response(data=msg, ok=False), http.INTERNAL_SERVER_ERROR
        return response(data=f"Success deleting {_id}", ok=True), http.OK
    except Exception as e:
        return response(data=f"Error: {e}", ok=False), http.BAD_REQUEST


def get(db_name, _id):
    collection = MONGO.db[db_name]
    try:
        data = db_result_to_json(collection.find({"_id": ObjectId(_id)}))
        return response(data=data, ok=True), http.OK
    except ValueError as e:
        return response(data=f"Error: {e}", ok=False), http.BAD_REQUEST


def get_all(db_name, args):
    collection = MONGO.db[db_name]
    try:
        data = db_result_to_json(collection.find(args))
        return response(data=data, ok=True), http.OK
    except ValueError as e:
        return response(data=f"Value error: {e}", ok=False), http.BAD_REQUEST
    except TypeError as e:
        return response(data=f"Type error: {e}", ok=False), http.BAD_REQUEST


def post(db_name, data):
    if not data:
        return response("Invalid request body", ok=False), http.BAD_REQUEST
    collection = MONGO.db[db_name]
    result = collection.insert_one(data)
    if not result.acknowledged:
        msg = 'write concern was disabled'
        return response(msg, ok=False), http.INTERNAL_SERVER_ERROR
    return response(data=str(result.inserted_id), ok=True), http.OK


def patch(db_name, data):
    if not data:
        return response("Invalid request body", ok=False), http.BAD_REQUEST
    _id = data.get('_id')
    collection = MONGO.db[db_name]
    collection.update({"_id": _id}, data)
    return response(data=str(_id), ok=True), http.OK


def validate_args(data, schema):
    for key in schema:
        if key not in data:
            raise ValueError(f"Argument {key} invalid")
        if not isinstance(data[key], schema[key]):
            raise ValueError(f"Argument {key} invalid type")


def validate_type(data, schema):
    for key in schema:
        if not isinstance(data[key], schema[key]):
            raise TypeError(f"Argument {key} has invalid type")
