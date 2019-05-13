import json
from http import HTTPStatus as http


def test_unregistered_user(client):
    resp = client.post('/session/', data=json.dumps({
        'email': 'someone@gmail.com',
        'password': '1234'
    }), content_type='application/json')
    assert not resp.json['ok']
    assert resp.status_code == http.BAD_REQUEST
    assert resp.json['data'] == "user does not exist"


def test_login_of_registered_user(client, random_user):
    user_data, secret = random_user
    resp = client.post('/session/', data=json.dumps({
        'email': user_data['email'],
        'password': secret
    }), content_type='application/json')
    assert resp.json['ok']
    assert resp.status_code == http.OK
