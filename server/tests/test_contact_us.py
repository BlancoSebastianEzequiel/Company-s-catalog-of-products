import json
from http import HTTPStatus


def test_contact_us_of_posted_user(client):
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
    resp = client.post('/contact_us/', data=json.dumps({
        'email': email,
        'password': secret,
        'subject': 'Discount',
        'message': 'How can i get a discount?'
    }), content_type='application/json')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.CREATED


def test_contact_us_with_bad_email(client):
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
    resp = client.post('/contact_us/', data=json.dumps({
        'email': 'bad_email',
        'password': '1234',
        'subject': 'Discount',
        'message': 'How can i get a discount?'
    }), content_type='application/json')
    assert not resp.json['ok']
    assert resp.status_code == HTTPStatus.BAD_REQUEST
