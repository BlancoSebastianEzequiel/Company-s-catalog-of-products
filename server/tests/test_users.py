import json
from server.controller.utils import check_password
from http import HTTPStatus

id_random = '5cdb89cec2d628266732962f'


def test_with_client(client):
    resp = client.get('/')
    assert resp.status_code == HTTPStatus.OK
    assert resp.json['test']


def test_list_users_initially_empty(client):
    resp = client.get('/users/')
    assert not resp.json['data']
    assert isinstance(resp.json['data'], list)


def test_get_not_existing_user_by_id(client):
    resp = client.get('/users/' + id_random + '/')
    assert resp.status_code == HTTPStatus.OK
    assert resp.json['ok']
    assert resp.json['data'] is None


def test_list_users_size_one_after_post_user(client):
    secret = '1234'
    resp = client.post('/users/', data=json.dumps({
        'first_name': 'juan',
        'last_name': 'perez',
        'user_name': 'juanchi',
        'email': 'juanperez@gmail.com',
        'password': secret,
        'type': 'client'
    }), content_type='application/json')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.CREATED
    resp = client.get('/users/')
    assert len(resp.json['data']) == 1
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.OK
    assert check_password(secret, resp.json['data'][0]['password'])


def test_get_user_with_unmatched_query(client):
    secret = '1234'
    resp = client.post('/users/', data=json.dumps({
        'first_name': 'juan',
        'last_name': 'perez',
        'user_name': 'juanchi',
        'email': 'juanperez@gmail.com',
        'password': secret,
        'type': 'client'
    }), content_type='application/json')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.CREATED
    resp = client.get('/users/?email="nada"')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.OK
    assert len(resp.json['data']) == 0


def test_get_user_with_good_query(client):
    secret = '1234'
    resp = client.post('/users/', data=json.dumps({
        'first_name': 'juan',
        'last_name': 'perez',
        'user_name': 'juanchi',
        'email': 'juanperez@gmail.com',
        'password': secret,
        'type': 'client'
    }), content_type='application/json')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.CREATED
    resp = client.get('/users/?email=juanperez@gmail.com')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.OK
    assert len(resp.json['data']) == 1


def test_post_user_with_no_first_name(client):
    resp = client.post('/users/', data=json.dumps({
        'last_name': 'perez',
        'user_name': 'juanchi',
        'email': 'juanperez@gmail.com',
        'password': '1234',
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
        'type': 'admin'
    }), content_type='application/json')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.CREATED
    _id = resp.json['data']
    resp = client.delete('/users/' + _id + '/')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.OK


def test_deleting_not_existent_user(client):
    bad_id = 'fafafafafafafafafafafafa'  # fake mongo 24-char hex string
    resp = client.delete('/users/' + bad_id + '/')
    assert not resp.json['ok']
    assert resp.status_code == HTTPStatus.BAD_REQUEST


def test_delete_user_invalid_id(client):
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
        'type': 'client'
    }), content_type='application/json')
    assert post_resp.json['ok']
    assert post_resp.status_code == HTTPStatus.CREATED
    _id = post_resp.json['data']

    patch_resp = client.patch('/users/', data=json.dumps({
        '_id': _id,
        'first_name': 'new name',
    }), content_type='application/json')
    assert patch_resp.json['ok']
    assert patch_resp.status_code == HTTPStatus.CREATED
    assert patch_resp.json['data'] == _id

    get_resp = client.get('/users/')
    assert get_resp.json['ok']
    assert get_resp.status_code == HTTPStatus.OK
    assert get_resp.json['data'][0]['first_name'] == 'new name'


def test_post_two_users_with_same_user_name_is_not_allowed(client):
    post_resp = client.post('/users/', data=json.dumps({
        'first_name': 'juan',
        'last_name': 'perez',
        'user_name': 'batman',
        'email': 'juanperez@gmail.com',
        'password': '1234',
        'type': 'client'
    }), content_type='application/json')
    assert post_resp.json['ok']
    assert post_resp.status_code == HTTPStatus.CREATED
    post_resp = client.post('/users/', data=json.dumps({
        'first_name': 'fabian',
        'last_name': 'gomez',
        'user_name': 'batman',
        'email': 'fabiangomez@gmail.com',
        'password': '1234',
        'type': 'client'
    }), content_type='application/json')
    assert not post_resp.json['ok']
    assert post_resp.status_code == HTTPStatus.BAD_REQUEST


def test_post_two_users_with_same_email_is_not_allowed(client):
    post_resp = client.post('/users/', data=json.dumps({
        'first_name': 'juan',
        'last_name': 'perez',
        'user_name': 'batman',
        'email': 'juanperez@gmail.com',
        'password': '1234',
        'type': 'client'
    }), content_type='application/json')
    assert post_resp.json['ok']
    assert post_resp.status_code == HTTPStatus.CREATED
    post_resp = client.post('/users/', data=json.dumps({
        'first_name': 'fabian',
        'last_name': 'gomez',
        'user_name': 'robin',
        'email': 'juanperez@gmail.com',
        'password': '1234',
        'type': 'client'
    }), content_type='application/json')
    assert not post_resp.json['ok']
    assert post_resp.status_code == HTTPStatus.BAD_REQUEST


def test_get_user_without_logging_in(auth_client):
    resp = auth_client.get('/users/')
    assert resp.status_code == HTTPStatus.UNAUTHORIZED
    assert not resp.json['ok']


def test_get_user_after_logging_in(auth_client):
    post_resp = auth_client.post('/users/', data=json.dumps({
        'first_name': 'juan',
        'last_name': 'perez',
        'user_name': 'batman',
        'email': 'juanperez@gmail.com',
        'password': '1234',
        'type': 'client'
    }), content_type='application/json')
    assert post_resp.json['ok']
    assert post_resp.status_code == HTTPStatus.CREATED
    login_resp = auth_client.post('/session/', data=json.dumps({
        'email': 'juanperez@gmail.com',
        'password': '1234'
    }), content_type='application/json')
    assert login_resp.json['ok']
    assert login_resp.status_code == HTTPStatus.CREATED
    token = login_resp.json['data']
    get_resp = auth_client.get(
        '/users/',
        headers={'Authorization': 'Bearer ' + token}
    )
    assert get_resp.status_code == HTTPStatus.OK
    assert get_resp.json['ok']


def test_post_user_with_missing_arguments(client):
    post_resp = client.post('/users/', data=json.dumps({
        'last_name': 'perez',
        'user_name': 'batman',
        'email': 'juanperez@gmail.com',
        'password': '1234',
        'type': 'client'
    }), content_type='application/json')
    assert not post_resp.json['ok']
    assert post_resp.status_code == HTTPStatus.BAD_REQUEST


def test_post_user_with_missing_password(client):
    post_resp = client.post('/users/', data=json.dumps({
        'first_name': 'juan',
        'last_name': 'perez',
        'user_name': 'batman',
        'email': 'juanperez@gmail.com',
        'type': 'client'
    }), content_type='application/json')
    assert not post_resp.json['ok']
    assert post_resp.status_code == HTTPStatus.BAD_REQUEST


def test_update_user_password(client):
    post_resp = client.post('/users/', data=json.dumps({
        'first_name': 'juan',
        'last_name': 'perez',
        'user_name': 'batman',
        'email': 'juanperez@gmail.com',
        'password': '1234',
        'type': 'client'
    }), content_type='application/json')
    assert post_resp.json['ok']
    assert post_resp.status_code == HTTPStatus.CREATED
    _id = post_resp.json['data']

    patch_resp = client.patch('/users/', data=json.dumps({
        '_id': _id,
        'password': '2',
    }), content_type='application/json')
    assert patch_resp.json['ok']
    assert patch_resp.status_code == HTTPStatus.CREATED
    assert patch_resp.json['data'] == _id

    get_resp = client.get(f'/users/{_id}/')
    assert get_resp.json['ok']
    assert get_resp.status_code == HTTPStatus.OK
    assert check_password('2', get_resp.json['data']['password'])


def test_user_email_bad_format(client):
    resp = client.post('/users/', data=json.dumps({
        'first_name': 'juan',
        'last_name': 'perez',
        'user_name': 'juanchi',
        'email': 'juanperez',
        'password': '1234',
        'type': 'client'
    }), content_type='application/json')
    assert not resp.json['ok']
    assert resp.status_code == HTTPStatus.BAD_REQUEST


def test_user_first_name_bad_format(client):
    resp = client.post('/users/', data=json.dumps({
        'first_name': 'juanchito22',
        'last_name': 'perez',
        'user_name': 'juanchi',
        'email': 'juanperez@gmail.com',
        'password': '1234',
        'type': 'client'
    }), content_type='application/json')
    assert not resp.json['ok']
    assert resp.status_code == HTTPStatus.BAD_REQUEST


def test_user_type_name_bad_format(client):
    resp = client.post('/users/', data=json.dumps({
        'first_name': 'juanchito',
        'last_name': 'perez',
        'user_name': 'juanchi',
        'email': 'juanperez@gmail.com',
        'password': '1234',
        'type': 'cliente'
    }), content_type='application/json')
    assert not resp.json['ok']
    assert resp.status_code == HTTPStatus.BAD_REQUEST


def test_update_user_with_bad_first_name_format(client):
    post_resp = client.post('/users/', data=json.dumps({
        'first_name': 'juanchito',
        'last_name': 'perez',
        'user_name': 'juanchi',
        'email': 'juanperez@gmail.com',
        'password': '1234',
        'type': 'client'
    }), content_type='application/json')
    assert post_resp.json['ok']
    assert post_resp.status_code == HTTPStatus.CREATED
    _id = post_resp.json['data']

    patch_resp = client.patch('/users/', data=json.dumps({
        '_id': _id,
        'first_name': '33',
        'last_name': 'perez',
        'user_name': 'juanchi',
        'email': 'juanperez@gmail.com',
        'password': '1234',
        'type': 'client'
    }), content_type='application/json')
    assert not patch_resp.json['ok']
    assert patch_resp.status_code == HTTPStatus.BAD_REQUEST


def test_update_user_with_bad_type_name_format(client):
    post_resp = client.post('/users/', data=json.dumps({
        'first_name': 'juan',
        'last_name': 'perez',
        'user_name': 'juanchi',
        'email': 'juanperez@gmail.com',
        'password': '1234',
        'type': 'client'
    }), content_type='application/json')
    assert post_resp.json['ok']
    assert post_resp.status_code == HTTPStatus.CREATED
    _id = post_resp.json['data']

    patch_resp = client.patch('/users/', data=json.dumps({
        '_id': _id,
        'first_name': 'juan',
        'last_name': 'perez',
        'user_name': 'juanchi',
        'email': 'juanperez@gmail.com',
        'password': '1234',
        'type': 'cliente'
    }), content_type='application/json')
    assert not patch_resp.json['ok']
    assert patch_resp.status_code == HTTPStatus.BAD_REQUEST
