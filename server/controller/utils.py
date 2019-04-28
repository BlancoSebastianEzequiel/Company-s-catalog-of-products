from flask import jsonify
from server.libs.mongo import MONGO


# pylint: disable=C0103
def response(data: str, ok: bool, **kwargs):
    """Arma una respuesta json generica"""
    return jsonify({'data': data, 'ok': ok, **kwargs})


def cursor_to_json(cursor):
    return [jsonify(instance) for instance in cursor]


def delete(db_name, _id):
    collection = MONGO.db[db_name]
    try:
        collection.deleteOne({"_id": _id})
    except ValueError as e:
        return response(data=f"does not exist: {e}", ok=False), 400


def get(db_name, _id):
    collection = MONGO.db[db_name]
    try:
        return collection.find({"_id": _id})
    except ValueError as e:
        return response(data=f"Error in getting doc: {e}", ok=False), 400


def get_all(db_name, args):
    collection = MONGO.db[db_name]
    try:
        data = cursor_to_json(collection.find(args))
        return response(data=data, ok=True), 400
    except ValueError as e:
        return response(data=f"Value error: {e}", ok=False), 400
    except TypeError as e:
        return response(data=f"Type error: {e}", ok=False), 400


def post(db_name, data):
    if not data:
        return response("Invalid or empty request body", ok=False), 400
    collection = MONGO.db[db_name]
    _id = collection.insert_one(data).inserted_id
    return str(_id)


def patch(db_name, data):
    if not data:
        return response("Invalid or empty request body", ok=False), 400
    _id = data.get('_id')
    collection = MONGO.db[db_name]
    collection.update({"_id": _id}, data)
    return None


def validate_args(args, schema):
    for key in args:
        if key not in schema:
            raise ValueError(f"Argument {key} invalid")
        if not isinstance(args[key], schema[key]):
            raise ValueError(f"Argument {key} invalid type")
