import json
from http import HTTPStatus


def test_with_client(client):
    resp = client.get('/')
    assert resp.status_code == HTTPStatus.OK
    assert resp.json['test']


def test_list_users_initially_empty(client):
    resp = client.get('/users/')
    assert not resp.json['data']
    assert isinstance(resp.json['data'], list)


def test_list_users_size_one_after_post_user(client):
    resp = client.post('/users/', data=json.dumps({
        'first_name': 'juan',
        'last_name': 'perez',
        'user_name': 'juanchi',
        'mail': 'juanperez@gmail.com',
        'password': '1234',
        'dni': '39206786',
    }), content_type='application/json')
    assert resp.json['ok']
    resp = client.get('/users/')
    assert len(resp.json['data']) == 1


def test_post_user_with_no_first_name(client):
    resp = client.post('/users/', data=json.dumps({
        'last_name': 'perez',
        'user_name': 'juanchi',
        'mail': 'juanperez@gmail.com',
        'password': '1234',
        'dni': '39206786',
    }), content_type='application/json')
    assert not resp.json['ok']
    assert resp.status_code == HTTPStatus.BAD_REQUEST


def test_post_user_with_first_name_invalid_type(client):
    resp = client.post('/users/', data=json.dumps({
        'first_name': 3,
        'last_name': 'perez',
        'user_name': 'juanchi',
        'mail': 'juanperez@gmail.com',
        'password': '1234',
        'dni': '39206786',
    }), content_type='application/json')
    assert not resp.json['ok']
    assert resp.status_code == HTTPStatus.BAD_REQUEST


def test_deleting_posted_user(client):
    resp = client.post('/users/', data=json.dumps({
        'first_name': 'juan',
        'last_name': 'perez',
        'user_name': 'juanchi',
        'mail': 'juanperez@gmail.com',
        'password': '1234',
        'dni': '39206786',
    }), content_type='application/json')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.OK
    _id = resp.json['data']
    resp = client.delete('/users/' + _id + '/')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.OK
