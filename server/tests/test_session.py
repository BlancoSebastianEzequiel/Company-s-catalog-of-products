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
    resp = client.post(
        '/users/',
        data=json.dumps(random_user),
        content_type='application/json'
    )
    assert resp.status_code == http.CREATED
    assert resp.json['ok']

    resp = client.post('/session/', data=json.dumps({
        'email': random_user['email'],
        'password': random_user['password']
    }), content_type='application/json')
    assert resp.json['ok']
    assert resp.status_code == http.CREATED


def test_login_auth_of_registered_user(auth_client):
    post_resp = auth_client.post('/users/', data=json.dumps({
        'first_name': 'juan',
        'last_name': 'perez',
        'user_name': 'juanchi',
        'email': 'juanperez@gmail.com',
        'password': '1234',
        'type': 'admin'
    }), content_type='application/json')
    assert post_resp.json['ok']
    assert post_resp.status_code == http.CREATED

    session_resp = auth_client.post('/session/', data=json.dumps({
        'email': 'juanperez@gmail.com',
        'password': '1234'
    }), content_type='application/json')
    assert session_resp.json['ok']
    assert session_resp.status_code == http.CREATED

    get_resp = auth_client.get('/users/', headers={
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + session_resp.json['data']
    })
    assert get_resp.json['ok']
    assert len(get_resp.json['data']) == 1
    assert get_resp.json['data'][0]['_id'] == post_resp.json['data']
