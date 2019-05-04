from server.libs.mongo import JSONEncoder
from server.libs.mongo import MONGO
from bson import ObjectId
from http import HTTPStatus as http
from server.exceptions.status_exception import StatusException


class Model:
    # Schema to validate the documents against. Keys: field names
    # values: types to validate against (use Python's typing module)
    schema = {}

    # Mongodb database name. Try to keep this unique between models!
    db_name = None

    def __init__(self, data: dict, _id=None):
        if "_id" in data.keys():
            data.pop("_id")
        self.validate_schema(data)
        self.validate_args(data)
        self.validate_type(data)
        self._data = data.copy()
        self._id = _id

    def valid_keys(self):
        return list(self.schema.keys()) + ['_id']

    def delete(self):
        try:
            collection = MONGO.db[self.db_name]
            result = collection.delete_one({"_id": ObjectId(self._id)})
            if not result.deleted_count and result.acknowledged:
                e = StatusException("Error deleting")
                e.status = http.INTERNAL_SERVER_ERROR
                raise e
            return self._id
        except Exception as ex:
            e = StatusException(ex)
            e.status = http.INTERNAL_SERVER_ERROR
            raise e

    @classmethod
    def get(cls, _id):
        try:
            ObjectId(_id)
        except Exception as ex:
            e = StatusException(ex)
            e.status = http.BAD_REQUEST
            raise e
        try:
            collection = MONGO.db[cls.db_name]
            doc = collection.find_one({"_id": ObjectId(_id)})
        except Exception as ex:
            e = StatusException(ex)
            e.status = http.INTERNAL_SERVER_ERROR
            raise e
        if doc is None:
            e = StatusException(f"{cls.db_name} {_id} does not exist")
            e.status = http.BAD_REQUEST
            raise e
        try:
            doc = dict(doc)
            model = cls(doc, doc["_id"])
            return model
        except Exception as ex:
            e = StatusException(ex)
            e.status = http.INTERNAL_SERVER_ERROR
            raise e

    @classmethod
    def get_all(cls, args: dict):
        try:
            collection = MONGO.db[cls.db_name]
            result = list(collection.find(args))
            data = [cls(doc, doc['_id'])._data for doc in result]
            return data
        except Exception as ex:
            e = StatusException(ex)
            e.status = http.INTERNAL_SERVER_ERROR
            raise e

    def post(self):
        try:
            collection = MONGO.db[self.db_name]
            result = collection.insert_one(self._data)
            if not result.acknowledged:
                e = StatusException('write concern was disabled')
                e.status = http.INTERNAL_SERVER_ERROR
                raise e
            self._id = result.inserted_id
            return self._id
        except Exception as ex:
            e = StatusException(ex)
            e.status = http.INTERNAL_SERVER_ERROR
            raise e

    def patch(self, data):
        try:
            if not data:
                e = StatusException("Invalid request body")
                e.status = http.BAD_REQUEST
                raise e
            collection = MONGO.db[self.db_name]
            collection.update_one({'_id': self._id}, {"$set": data})
            return self._id
        except Exception as ex:
            e = StatusException(ex)
            e.status = http.INTERNAL_SERVER_ERROR
            raise e

    def validate_args(self, data):
        a_list = list(data.keys())
        keys = self.valid_keys()
        keys_to_drop = list(filter(lambda x: x not in keys, a_list))
        for key in keys_to_drop:
            data.pop(key)

    def validate_type(self, data):
        for key in data:
            if not isinstance(data[key], self.schema[key]):
                e = StatusException(f"Argument {key} has invalid type")
                e.status = http.BAD_REQUEST
                raise e

    def validate_schema(self, data):
        for key in self.schema:
            if key not in data:
                e = StatusException(f"Argument {key} missing")
                e.status = http.BAD_REQUEST
                raise e

    def to_json(self):
        data = self._data.copy()
        return JSONEncoder().encode(data)
