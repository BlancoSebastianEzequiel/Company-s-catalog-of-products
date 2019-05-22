from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

SECRET_KEY = 's3cr3t'
TOKEN_SERIALIZER = Serializer(SECRET_KEY, expires_in=3600)
COMPANY_EMAIL = "ACPI.company.catalog.of.products@gmail.com"
EMAIL_PASSWORD = "ACPI/SRL/1234"
