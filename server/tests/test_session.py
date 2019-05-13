import json
from http import HTTPStatus as http


def test_unregistered_user(client):
    resp = client.post('/session/', data=json.dumps({
        'email': 'someone@gmail.com',
        'password': '1234'
    }), content_type='application/json')
    print(f"resp.json: {resp.json}")
    assert not resp.json['ok']
    assert resp.status_code == http.BAD_REQUEST
    assert resp.json['data'] == "user does not exist"
