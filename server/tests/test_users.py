import json


def test_with_client(client):
    resp = client.get('/')
    assert resp.status_code == 200
    assert resp.json['test']


def test_list_users_initially_empty(client):
    resp = client.get('/users/')
    assert not resp.json['data']
    assert isinstance(resp.json['data'], list)


def test_list_users_size_one_after_post_user(client):
    client.post('/users/', data=json.dumps({
        'first_name': 'Juan',
        'last_name': 'perez',
        'user_name': 'juanchi',
        'mail': 'juanperez@gmail.com',
        'password': '1234',
        'dni': '39206786',
    }), content_type='application/json')
    resp = client.get('/users/')
    assert len(resp.json['data']) == 1
