from server.libs.mongo import JSONEncoder
from server.libs.mongo import MONGO
from bson import ObjectId


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
        collection = MONGO.db[self.db_name]
        result = collection.delete_one({"_id": ObjectId(self._id)})
        if not result.deleted_count and result.acknowledged:
            raise Exception("Error deleting")
        return self._id

    @classmethod
    def get(cls, _id):
        collection = MONGO.db[cls.db_name]
        doc = collection.find({"_id": ObjectId(_id)})[0]
        if not doc:
            raise Exception(f"{cls.db_name} {_id} does not exist")
        doc = dict(doc)
        model = cls(doc, doc["_id"])
        return model

    @classmethod
    def get_all(cls, args: dict):
        collection = MONGO.db[cls.db_name]
        result = list(collection.find(args))
        data = [cls(doc, doc['_id'])._data for doc in result]
        return data

    def post(self):
        collection = MONGO.db[self.db_name]
        result = collection.insert_one(self._data)
        if not result.acknowledged:
            raise Exception('write concern was disabled')
        self._id = result.inserted_id
        return self._id

    def patch(self, data):
        if not data:
            raise Exception("Invalid request body")
        collection = MONGO.db[self.db_name]
        collection.update_one({'_id': self._id}, {"$set": data})
        return self._id

    def validate_args(self, data):
        a_list = list(data.keys())
        keys = self.valid_keys()
        keys_to_drop = list(filter(lambda x: x not in keys, a_list))
        for key in keys_to_drop:
            data.pop(key)

    def validate_type(self, data):
        for key in data:
            if not isinstance(data[key], self.schema[key]):
                raise TypeError(f"Argument {key} has invalid type")

    def validate_schema(self, data):
        for key in self.schema:
            if key not in data:
                raise ValueError(f"Argument {key} missing")

    def to_json(self):
        data = self._data.copy()
        return JSONEncoder().encode(data)