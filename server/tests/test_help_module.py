import json
from http import HTTPStatus

id_random = '5cdb89cec2d628266732962f'


def test_list_help_module_initially_empty(client):
    resp = client.get('/help_module/')
    assert not resp.json['data']
    assert isinstance(resp.json['data'], list)


def test_get_not_existing_user_by_id(client):
    resp = client.get('/help_module/' + id_random + '/')
    assert resp.status_code == HTTPStatus.OK
    assert resp.json['ok']
    assert resp.json['data'] is None


def test_list_size_one_after_post_help_module(client):
    resp = client.post('/help_module/', data=json.dumps({
        'title': 'Register',
        'description': 'To register you have to...'
    }), content_type='application/json')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.CREATED
    resp = client.get('/help_module/')
    assert len(resp.json['data']) == 1
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.OK


def test_get_help_modulewith_unmatched_query(client):
    resp = client.post('/help_module/', data=json.dumps({
        'title': 'Register',
        'description': 'To register you have to...'
    }), content_type='application/json')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.CREATED
    resp = client.get('/help_module/?quantity_of_employees=201')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.OK
    assert len(resp.json['data']) == 0


def test_get_help_module_with_good_query(client):
    resp = client.post('/help_module/', data=json.dumps({
        'title': 'Register',
        'description': 'To register you have to...'
    }), content_type='application/json')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.CREATED
    resp = client.get('/help_module/?title=Register')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.OK
    assert len(resp.json['data']) == 1


def test_post_help_module_with_no_title(client):
    resp = client.post('/help_module/', data=json.dumps({
        'description': 'To register you have to...'
    }), content_type='application/json')
    assert not resp.json['ok']
    assert resp.status_code == HTTPStatus.BAD_REQUEST


def test_post_help_module_with_title_invalid_type(client):
    resp = client.post('/help_module/', data=json.dumps({
        'title': 33,
        'description': 'To register you have to...'
    }), content_type='application/json')
    assert not resp.json['ok']
    assert resp.status_code == HTTPStatus.BAD_REQUEST


def test_deleting_posted_help_module(client):
    resp = client.post('/help_module/', data=json.dumps({
        'title': 'Register',
        'description': 'To register you have to...'
    }), content_type='application/json')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.CREATED
    _id = resp.json['data']
    resp = client.delete('/help_module/' + _id + '/')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.OK


def test_deleting_not_existent_help_module(client):
    bad_id = 'fafafafafafafafafafafafa'  # fake mongo 24-char hex string
    resp = client.delete('/help_module/' + bad_id + '/')
    assert not resp.json['ok']
    assert resp.status_code == HTTPStatus.BAD_REQUEST


def test_delete_help_module_invalid_id(client):
    bad_id = "not hex wrong len"
    resp = client.delete(f'/help_module/{bad_id}/')
    assert resp.status_code == HTTPStatus.BAD_REQUEST


def test_updating_help_module(client):
    post_resp = client.post('/help_module/', data=json.dumps({
        'title': 'Register',
        'description': 'To register you have to...'
    }), content_type='application/json')
    assert post_resp.json['ok']
    assert post_resp.status_code == HTTPStatus.CREATED
    _id = post_resp.json['data']

    patch_resp = client.patch('/help_module/', data=json.dumps({
        '_id': _id,
        'title': 'Client Registration',
    }), content_type='application/json')
    assert patch_resp.json['ok']
    assert patch_resp.status_code == HTTPStatus.CREATED
    assert patch_resp.json['data'] == _id

    get_resp = client.get('/help_module/')
    assert get_resp.json['ok']
    assert get_resp.status_code == HTTPStatus.OK
    assert get_resp.json['data'][0]['title'] == 'Client Registration'


def test_get_help_module_without_logging_in(auth_client):
    resp = auth_client.get('/help_module/')
    assert resp.status_code == HTTPStatus.UNAUTHORIZED
    assert not resp.json['ok']


def test_post_help_module_with_missing_arguments(client):
    post_resp = client.post('/help_module/', data=json.dumps({
        'description': 'To register you have to...'
    }), content_type='application/json')
    assert not post_resp.json['ok']
    assert post_resp.status_code == HTTPStatus.BAD_REQUEST


def test_update_help_module_with_the_same_data(client):
    post_resp = client.post('/help_module/', data=json.dumps({
        'title': 'Register',
        'description': 'To register you have to...'
    }), content_type='application/json')
    assert post_resp.json['ok']
    assert post_resp.status_code == HTTPStatus.CREATED
    _id = post_resp.json['data']

    patch_resp = client.patch('/help_module/', data=json.dumps({
        '_id': _id,
        'title': 'Register',
        'description': 'To register you have to...'
    }), content_type='application/json')
    assert patch_resp.json['ok']
    assert patch_resp.status_code == HTTPStatus.CREATED


def test_get_help_module_with_query(client):
    post_resp = client.post('/help_module/', data=json.dumps({
        'title': 'Register',
        'description': 'To register you have to...'
    }), content_type='application/json')
    assert post_resp.json['ok']
    assert post_resp.status_code == HTTPStatus.CREATED

    query = "/help_module/?title=Register"
    get_resp = client.get(query)
    assert get_resp.json['ok']
    assert get_resp.status_code == HTTPStatus.OK


def test_client_post_help_module_is_not_allowed(auth_client):
    resp = auth_client.post('/users/', data=json.dumps({
        'first_name': 'juan',
        'last_name': 'perez',
        'user_name': 'juanchi',
        'email': 'juanperez@gmail.com',
        'password': '1234',
        'type': 'client'
    }), content_type='application/json')
    assert resp.status_code == HTTPStatus.CREATED
    assert resp.json['ok']

    resp = auth_client.post('/session/', data=json.dumps({
        'email': 'juanperez@gmail.com',
        'password': '1234'
    }), content_type='application/json')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.CREATED
    token = resp.json['data']

    resp = auth_client.post('/help_module/', data=json.dumps({
        'title': 'Register',
        'description': 'To register you have to...'}),
        content_type='application/json',
        headers={'Authorization': 'Bearer ' + token}
    )
    assert not resp.json['ok']
    assert resp.status_code == HTTPStatus.UNAUTHORIZED


def test_admin_post_help_module_is_allowed(auth_client):
    resp = auth_client.post('/users/', data=json.dumps({
        'first_name': 'juan',
        'last_name': 'perez',
        'user_name': 'juanchi',
        'email': 'juanperez@gmail.com',
        'password': '1234',
        'type': 'admin'
    }), content_type='application/json')
    assert resp.status_code == HTTPStatus.CREATED
    assert resp.json['ok']

    resp = auth_client.post('/session/', data=json.dumps({
        'email': 'juanperez@gmail.com',
        'password': '1234'
    }), content_type='application/json')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.CREATED
    token = resp.json['data']

    resp = auth_client.post('/help_module/', data=json.dumps({
        'title': 'Register',
        'description': 'To register you have to...'}),
        content_type='application/json',
        headers={'Authorization': 'Bearer ' + token}
    )
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.CREATED
