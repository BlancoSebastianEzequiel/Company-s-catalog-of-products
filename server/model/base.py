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

    # key: field of schema
    # value: boolean. if true the values cannot be repeated in the db
    unique_values = {}

    # key: field of schema
    # value: function. if false the value does not meet the required format
    validation = {}

    def __init__(self, data: dict, _id=None, unique_values=False):
        self.validate_data(data, unique_values)
        self._data = data.copy()
        self._id = _id
        self.validate_schema_format(self._data)

    def __getitem__(self, item):
        self.validate_key_in_schema(item)
        return self._data.get(item)

    def get_data(self):
        return self._data.copy()

    def __setitem__(self, field, value):
        self.validate_key_in_schema(field)
        self.validate_type(field, value)
        self._data[field] = value

    def built_validator_schema(self):
        self.validation = {}

    @classmethod
    def validate_schema_format(cls, data):
        for field in cls.validation:
            if field not in data:
                continue
            value = data[field]
            callback = cls.validation[field]
            name = cls.__class__.__name__
            cls.validate_value_format(value, callback, name, field)

    @staticmethod
    def validate_value_format(value, callback, field, name):
        if not callback(value):
            msg = f"{field} does not meet the required format of {name}"
            raise StatusException(msg, http.BAD_REQUEST)

    @classmethod
    def validate_data(cls, data: dict, check_unique_values: bool):
        if "_id" in data.keys():
            data.pop("_id")
        cls.validate_schema(data)
        cls.validate_args(data)
        cls.validate_data_types(data)
        if check_unique_values:
            cls.validate_already_existing_unique_values(data)

    @classmethod
    def validate_update_data(cls, data: dict, check_unique_values: bool, _id):
        if "_id" in data.keys():
            data.pop("_id")
        cls.validate_args(data)
        cls.validate_data_types(data)
        if check_unique_values:
            cls.validate_already_existing_unique_values(data, _id)
        cls.validate_schema_format(data)

    @classmethod
    def validate_key_in_schema(cls, field):
        if field not in cls.schema.keys():
            name = cls.__class__.__name__
            e = StatusException(f"{field} is not a valid attribute of {name}")
            e.status = http.BAD_REQUEST
            raise e

    @classmethod
    def validate_type(cls, field, value):
        return isinstance(value, cls.schema[field])

    @classmethod
    def valid_keys(cls):
        return list(cls.schema.keys()) + ['_id']

    @classmethod
    def validate_already_existing_unique_values(cls, data, _id=None):
        for field in data:
            value = data[field]
            cls.check_unique_value(field, value, _id)

    @classmethod
    def check_unique_value(cls, field, value, _id=None):
        if not cls.unique_values[field]:
            return
        result = cls.get_all({field: value})
        if len(result) == 0:
            return
        if len(result) == 1 and _id is not None:
            if _id == str(result[0]['_id']):
                return
        msg = f"field {field} already exists"
        raise StatusException(msg, http.BAD_REQUEST)

    def delete(self):
        try:
            collection = MONGO.db[self.db_name]
            res = collection.delete_one({"_id": ObjectId(self._id)})
            if res.deleted_count != 1:
                msg = f"The number of deleted docs were {res.deleted_count}"
                e = StatusException(msg)
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
        if doc is not None:
            doc = dict(doc)
            cls.validate_data(doc, False)
        return doc

    @classmethod
    def get_all(cls, args: dict):
        try:
            collection = MONGO.db[cls.db_name]
            result = list(collection.find(args))
            return result
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
        self.validate_update_data(data, True, self._id)
        try:
            collection = MONGO.db[self.db_name]
            collection.update_one({'_id': ObjectId(self._id)}, {"$set": data})
            return self._id
        except Exception as ex:
            e = StatusException(ex)
            e.status = http.INTERNAL_SERVER_ERROR
            raise e

    @classmethod
    def validate_args(cls, data):
        a_list = list(data.keys())
        keys = cls.valid_keys()
        keys_to_drop = list(filter(lambda x: x not in keys, a_list))
        for key in keys_to_drop:
            data.pop(key)

    @classmethod
    def validate_data_types(cls, data):
        for key in data:
            if not cls.validate_type(key, data[key]):
                e = StatusException(f"Argument {key} has invalid type")
                e.status = http.BAD_REQUEST
                raise e

    @classmethod
    def validate_schema(cls, data):
        for key in cls.schema:
            if key not in data:
                e = StatusException(f"Argument {key} missing")
                e.status = http.BAD_REQUEST
                raise e

    def to_json(self):
        data = self._data.copy()
        return JSONEncoder().encode(data)
