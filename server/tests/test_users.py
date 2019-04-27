def test_with_client(client):
    resp = client.get('/')
    assert resp.status_code == 200
    assert resp.json['test']


def test_list_users_initially_empty(client):
    resp = client.get('/users/')
    assert not resp.json['data']
    assert isinstance(resp.json['data'], list)
