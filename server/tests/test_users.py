import json
from server.controller.utils import check_password
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
    secret = '1234'
    resp = client.post('/users/', data=json.dumps({
        'first_name': 'juan',
        'last_name': 'perez',
        'user_name': 'juanchi',
        'email': 'juanperez@gmail.com',
        'password': secret,
        'dni': '39206786',
        'type': 'client'
    }), content_type='application/json')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.OK
    resp = client.get('/users/')
    assert len(resp.json['data']) == 1
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.OK
    assert check_password(secret, resp.json['data'][0]['password'])


def test_post_user_with_no_first_name(client):
    resp = client.post('/users/', data=json.dumps({
        'last_name': 'perez',
        'user_name': 'juanchi',
        'email': 'juanperez@gmail.com',
        'password': '1234',
        'dni': '39206786',
        'type': 'client'
    }), content_type='application/json')
    assert not resp.json['ok']
    assert resp.status_code == HTTPStatus.BAD_REQUEST


def test_post_user_with_first_name_invalid_type(client):
    resp = client.post('/users/', data=json.dumps({
        'first_name': 3,
        'last_name': 'perez',
        'user_name': 'juanchi',
        'email': 'juanperez@gmail.com',
        'password': '1234',
        'dni': '39206786',
        'type': 'admin'
    }), content_type='application/json')
    assert not resp.json['ok']
    assert resp.status_code == HTTPStatus.BAD_REQUEST


def test_deleting_posted_user(client):
    resp = client.post('/users/', data=json.dumps({
        'first_name': 'juan',
        'last_name': 'perez',
        'user_name': 'juanchi',
        'email': 'juanperez@gmail.com',
        'password': '1234',
        'dni': '39206786',
        'type': 'admin'
    }), content_type='application/json')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.OK
    _id = resp.json['data']
    resp = client.delete('/users/' + _id + '/')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.OK


def test_deleting_not_existent_user(client):
    bad_id = 'fafafafafafafafafafafafa'  # fake mongo 24-char hex string
    resp = client.delete('/users/' + bad_id + '/')
    assert not resp.json['ok']
    assert resp.status_code == HTTPStatus.BAD_REQUEST


def test_delete_article_invalid_id(client):
    bad_id = "not hex wrong len"
    resp = client.delete(f'/users/{bad_id}/')
    assert resp.status_code == HTTPStatus.BAD_REQUEST


def test_updating_user(client):
    post_resp = client.post('/users/', data=json.dumps({
        'first_name': 'juan',
        'last_name': 'perez',
        'user_name': 'juanchi',
        'email': 'juanperez@gmail.com',
        'password': '1234',
        'dni': '39206786',
        'type': 'client'
    }), content_type='application/json')
    assert post_resp.json['ok']
    assert post_resp.status_code == HTTPStatus.OK
    _id = post_resp.json['data']

    patch_resp = client.patch('/users/', data=json.dumps({
        '_id': _id,
        'first_name': 'new name',
    }), content_type='application/json')
    assert patch_resp.json['ok']
    assert patch_resp.status_code == HTTPStatus.OK
    assert patch_resp.json['data'] == _id

    get_resp = client.get('/users/')
    assert get_resp.json['ok']
    assert get_resp.status_code == HTTPStatus.OK
    assert get_resp.json['data'][0]['first_name'] == 'new name'
