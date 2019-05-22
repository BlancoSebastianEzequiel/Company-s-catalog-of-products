import json
from http import HTTPStatus

id_random = '5cdb89cec2d628266732962f'


def test_list_products_initially_empty(client):
    resp = client.get('/products/')
    assert not resp.json['data']
    assert isinstance(resp.json['data'], list)


def test_get_not_existing_products_by_id(client):
    resp = client.get('/products/' + id_random + '/')
    assert resp.status_code == HTTPStatus.OK
    assert resp.json['ok']
    assert resp.json['data'] is None


def test_list_products_size_one_after_posting_product(client):
    resp = client.post('/products/', data=json.dumps({
        'code': '400',
        'name': 'ibu400',
        'description': 'Alivia el dolor de cabeza',
        'images': [],
        'size': '70ml',
        'active_principle': '20'
    }), content_type='application/json')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.CREATED
    resp = client.get('/products/')
    assert len(resp.json['data']) == 1
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.OK


def test_get_product_with_unmatched_query(client):
    resp = client.post('/products/', data=json.dumps({
        'code': '400',
        'name': 'ibu400',
        'description': 'Alivia el dolor de cabeza',
        'images': [],
        'size': '70ml',
        'active_principle': '20'
    }), content_type='application/json')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.CREATED
    resp = client.get('/products/?code=bad_code')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.OK
    assert len(resp.json['data']) == 0


def test_get_product_with_good_query(client):
    resp = client.post('/products/', data=json.dumps({
        'code': '400',
        'name': 'ibu400',
        'description': 'Alivia el dolor de cabeza',
        'images': [],
        'size': '70ml',
        'active_principle': '20'
    }), content_type='application/json')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.CREATED
    resp = client.get('/products/?code=400')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.OK
    assert len(resp.json['data']) == 1


def test_post_product_with_name_invalid_type(client):
    resp = client.post('/products/', data=json.dumps({
        'code': '400',
        'name': 400,
        'description': 'Alivia el dolor de cabeza',
        'images': [],
        'size': '70ml',
        'active_principle': '20'
    }), content_type='application/json')
    assert not resp.json['ok']
    assert resp.status_code == HTTPStatus.BAD_REQUEST


def test_deleting_posted_product(client):
    resp = client.post('/products/', data=json.dumps({
        'code': '400',
        'name': 'ibu400',
        'description': 'Alivia el dolor de cabeza',
        'images': [],
        'size': '70ml',
        'active_principle': '20'
    }), content_type='application/json')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.CREATED
    _id = resp.json['data']
    resp = client.delete('/products/' + _id + '/')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.OK


def test_deleting_not_existent_product(client):
    bad_id = 'fafafafafafafafafafafafa'  # fake mongo 24-char hex string
    resp = client.delete('/products/' + bad_id + '/')
    assert not resp.json['ok']
    assert resp.status_code == HTTPStatus.BAD_REQUEST


def test_delete_product_invalid_id(client):
    bad_id = "not hex wrong len"
    resp = client.delete(f'/products/{bad_id}/')
    assert resp.status_code == HTTPStatus.BAD_REQUEST


def test_updating_product(client):
    post_resp = client.post('/products/', data=json.dumps({
        'code': '400',
        'name': 'ibu400',
        'description': 'Alivia el dolor de cabeza',
        'images': [],
        'size': '70ml',
        'active_principle': '20'
    }), content_type='application/json')
    assert post_resp.json['ok']
    assert post_resp.status_code == HTTPStatus.CREATED
    _id = post_resp.json['data']

    patch_resp = client.patch('/products/', data=json.dumps({
        '_id': _id,
        'name': 'new name',
    }), content_type='application/json')
    assert patch_resp.json['ok']
    assert patch_resp.status_code == HTTPStatus.CREATED
    assert patch_resp.json['data'] == _id

    get_resp = client.get('/products/')
    assert get_resp.json['ok']
    assert get_resp.status_code == HTTPStatus.OK
    assert get_resp.json['data'][0]['name'] == 'new name'


def test_post_two_products_with_same_code_is_not_allowed(client):
    post_resp = client.post('/products/', data=json.dumps({
        'code': '400',
        'name': 'ibu400',
        'description': 'Alivia el dolor de cabeza',
        'images': [],
        'size': '70ml',
        'active_principle': '20'
    }), content_type='application/json')
    assert post_resp.json['ok']
    assert post_resp.status_code == HTTPStatus.CREATED
    post_resp = client.post('/products/', data=json.dumps({
        'code': '400',
        'name': 'ibu400',
        'description': 'Alivia el dolor de cabeza',
        'images': [],
        'size': '70ml',
        'active_principle': '20'
    }), content_type='application/json')
    assert not post_resp.json['ok']
    assert post_resp.status_code == HTTPStatus.BAD_REQUEST


def test_get_product_without_logging_in(auth_client):
    resp = auth_client.get('/products/')
    assert resp.status_code == HTTPStatus.UNAUTHORIZED
    assert not resp.json['ok']


def test_get_product_after_logging_in(auth_client):
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
        '/products/',
        headers={'Authorization': 'Bearer ' + token}
    )
    assert get_resp.status_code == HTTPStatus.OK
    assert get_resp.json['ok']


def test_post_product_with_missing_arguments(client):
    post_resp = client.post('/products/', data=json.dumps({
        'code': '400',
        'description': 'Alivia el dolor de cabeza',
        'images': [],
        'size': '70ml',
        'active_principle': '20'
    }), content_type='application/json')
    assert not post_resp.json['ok']
    assert post_resp.status_code == HTTPStatus.BAD_REQUEST
