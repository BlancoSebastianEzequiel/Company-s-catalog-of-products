from itsdangerous import URLSafeSerializer as Serializer

SECRET_KEY = 's3cr3t'
TOKEN_SERIALIZER = Serializer(SECRET_KEY)
COMPANY_EMAIL = "ACPI.company.catalog.of.products@gmail.com"
EMAIL_PASSWORD = "ACPI/SRL/1234"
