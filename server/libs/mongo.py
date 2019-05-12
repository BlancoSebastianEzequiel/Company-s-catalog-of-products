import datetime
import json
# pylint: disable=RP0401
from bson.objectid import ObjectId
from flask_pymongo import PyMongo

MONGO = PyMongo()


class JSONEncoder(json.JSONEncoder):
    # extend json encoder for compatibility with mongoDB
    def default(self, o):  # pylint: disable=E0202
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)
