from conf.local import Config as BaseConfig


class Config(BaseConfig):
    DEBUG = False
    SKIP_AUTH = False
    SKIP_SEND_EMAIL = False
