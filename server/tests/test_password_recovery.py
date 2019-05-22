import json
from http import HTTPStatus


def test_password_recovery_of_posted_user(client):
    secret = '1234'
    email = 'sebastian.e.blanco@gmail.com'
    resp = client.post('/users/', data=json.dumps({
        'first_name': 'juan',
        'last_name': 'perez',
        'user_name': 'juanchi',
        'email': email,
        'password': secret,
        'type': 'client'
    }), content_type='application/json')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.CREATED
    resp = client.get('/password_recovery/' + email + '/')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.OK


def test_password_recovery_with_not_bad_email(client):
    resp = client.post('/users/', data=json.dumps({
        'first_name': 'juan',
        'last_name': 'perez',
        'user_name': 'juanchi',
        'email': 'sebastian.e.blanco@gmailcom',
        'password': '1234',
        'type': 'client'
    }), content_type='application/json')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.CREATED
    resp = client.get('/password_recovery/' + 'bad_email' + '/')
    assert not resp.json['ok']
    assert resp.status_code == HTTPStatus.BAD_REQUEST


"""
def test_password_recovery_with_without_skipping_sending_email(auth_client):
    secret = '1234'
    email = 'sebastian.e.blanco@gmail.com'
    resp = auth_client.post('/users/', data=json.dumps({
        'first_name': 'juan',
        'last_name': 'perez',
        'user_name': 'juanchi',
        'email': email,
        'password': secret,
        'type': 'client'
    }), content_type='application/json')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.CREATED
    resp = auth_client.get('/password_recovery/' + email + '/')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.OK
"""
