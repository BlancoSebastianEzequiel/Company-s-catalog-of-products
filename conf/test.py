import os
from conf.local import Config as BaseConfig


class Config(BaseConfig):
    """
    Tests config class. Overrides base config class attributes necessary to
    run tests without affecting the real server's state
    """
    MONGO_URI = os.environ.get('DB', "mongodb://localhost:27018/testing")
