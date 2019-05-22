import json
from http import HTTPStatus

id_random = '5cdb89cec2d628266732962f'


def test_list_active_principle_initially_empty(client):
    resp = client.get('/active_principle/')
    assert not resp.json['data']
    assert isinstance(resp.json['data'], list)
    assert len(resp.json['data']) == 0


def test_get_not_existing_active_principle_by_id(client):
    resp = client.get('/active_principle/' + id_random + '/')
    assert resp.status_code == HTTPStatus.OK
    assert resp.json['ok']
    assert resp.json['data'] is None


def test_list_active_principle_size_one_after_post_user(client):
    resp = client.post('/active_principle/', data=json.dumps({
        'code': '1',
        'name': 'paracetamol',
        'description': 'analgésicos y antiinflamatorios'
    }), content_type='application/json')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.CREATED
    resp = client.get('/active_principle/')
    assert len(resp.json['data']) == 1
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.OK


def test_get_active_principle_with_unmatched_query(client):
    resp = client.post('/active_principle/', data=json.dumps({
        'code': '1',
        'name': 'paracetamol',
        'description': 'analgésicos y antiinflamatorios'
    }), content_type='application/json')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.CREATED
    resp = client.get('/active_principle/?code=2')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.OK
    assert len(resp.json['data']) == 0


def test_get_active_principle_with_good_query(client):
    resp = client.post('/active_principle/', data=json.dumps({
        'code': '1',
        'name': 'paracetamol',
        'description': 'analgésicos y antiinflamatorios'
    }), content_type='application/json')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.CREATED
    resp = client.get('/active_principle/?code=1')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.OK
    assert len(resp.json['data']) == 1


def test_post_active_principle_with_no_name(client):
    resp = client.post('/active_principle/', data=json.dumps({
        'code': '1',
        'description': 'analgésicos y antiinflamatorios'
    }), content_type='application/json')
    assert not resp.json['ok']
    assert resp.status_code == HTTPStatus.BAD_REQUEST


def test_post_active_principle_with_name_invalid_type(client):
    resp = client.post('/active_principle/', data=json.dumps({
        'code': '1',
        'name': 343,
        'description': 'analgésicos y antiinflamatorios'
    }), content_type='application/json')
    assert not resp.json['ok']
    assert resp.status_code == HTTPStatus.BAD_REQUEST


def test_deleting_active_principle(client):
    resp = client.post('/active_principle/', data=json.dumps({
        'code': '1',
        'name': 'paracetamol',
        'description': 'analgésicos y antiinflamatorios'
    }), content_type='application/json')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.CREATED
    _id = resp.json['data']
    resp = client.delete('/active_principle/' + _id + '/')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.OK


def test_deleting_not_existent_active_principle(client):
    bad_id = 'fafafafafafafafafafafafa'  # fake mongo 24-char hex string
    resp = client.delete('/active_principle/' + bad_id + '/')
    assert not resp.json['ok']
    assert resp.status_code == HTTPStatus.BAD_REQUEST


def test_delete_active_principle_invalid_id(client):
    bad_id = "not hex wrong len"
    resp = client.delete(f'/active_principle/{bad_id}/')
    assert resp.status_code == HTTPStatus.BAD_REQUEST


def test_updating_user(client):
    post_resp = client.post('/active_principle/', data=json.dumps({
        'code': '1',
        'name': 'paracetamol',
        'description': 'analgésicos y antiinflamatorios'
    }), content_type='application/json')
    assert post_resp.json['ok']
    assert post_resp.status_code == HTTPStatus.CREATED
    _id = post_resp.json['data']

    patch_resp = client.patch('/active_principle/', data=json.dumps({
        '_id': _id,
        'name': 'new name',
    }), content_type='application/json')
    assert patch_resp.json['ok']
    assert patch_resp.status_code == HTTPStatus.CREATED
    assert patch_resp.json['data'] == _id

    get_resp = client.get('/active_principle/')
    assert get_resp.json['ok']
    assert get_resp.status_code == HTTPStatus.OK
    assert get_resp.json['data'][0]['name'] == 'new name'


def test_post_two_active_principle_with_same_code_is_not_allowed(client):
    post_resp = client.post('/active_principle/', data=json.dumps({
        'code': '1',
        'name': 'paracetamol',
        'description': 'analgésicos y antiinflamatorios'
    }), content_type='application/json')
    assert post_resp.json['ok']
    assert post_resp.status_code == HTTPStatus.CREATED
    post_resp = client.post('/active_principle/', data=json.dumps({
        'code': '1',
        'name': 'ibu 400',
        'description': 'analgésicos y antiinflamatorios'
    }), content_type='application/json')
    assert not post_resp.json['ok']
    assert post_resp.status_code == HTTPStatus.BAD_REQUEST
