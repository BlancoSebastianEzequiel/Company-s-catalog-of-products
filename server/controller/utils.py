import smtplib
from flask import jsonify, current_app
from server.secrets import TOKEN_SERIALIZER, COMPANY_EMAIL, EMAIL_PASSWORD
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# pylint: disable=C0103
def response(data, ok, **kwargs):
    """Arma una respuesta json generica"""
    return jsonify({'data': data, 'ok': ok, **kwargs})


def get_hashed_password(secret_password):
    data = {'password': secret_password}
    return generate_token_from_data(data)


def check_password(secret_password, hashed):
    return secret_password == get_secret_password_from_hashed(hashed)


def get_secret_password_from_hashed(hashed):
    return get_data_from_token(hashed)['password']


def get_data_from_token(token):
    return TOKEN_SERIALIZER.loads(token)


def generate_token_from_data(data):
    return TOKEN_SERIALIZER.dumps(data)


def send_email(email_to, subject, message):
    if current_app.config['SKIP_SEND_EMAIL']:
        return
    # create message object instance
    msg = MIMEMultipart()
    # setup the parameters of the message
    msg['From'] = COMPANY_EMAIL
    msg['To'] = email_to
    msg['Subject'] = subject
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    # create server
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    # Login Credentials for sending the mail
    server.login(msg['From'], EMAIL_PASSWORD)
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
