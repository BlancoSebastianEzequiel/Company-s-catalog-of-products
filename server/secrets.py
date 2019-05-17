from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

SECRET_KEY = 's3cr3t'
TOKEN_SERIALIZER = Serializer(SECRET_KEY, expires_in=3600)
