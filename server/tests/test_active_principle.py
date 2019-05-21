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
        'code': 'juan',
        'name': 'perez',
        'description': 'juanchi'
    }), content_type='application/json')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.CREATED
    resp = client.get('/active_principle/')
    assert len(resp.json['data']) == 1
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.OK
