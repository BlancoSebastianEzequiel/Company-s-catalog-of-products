import json
from http import HTTPStatus

id_random = '5cdb89cec2d628266732962f'


def test_list_company_data_initially_empty(client):
    resp = client.get('/company_data/')
    assert not resp.json['data']
    assert isinstance(resp.json['data'], list)


def test_get_not_existing_user_by_id(client):
    resp = client.get('/company_data/' + id_random + '/')
    assert resp.status_code == HTTPStatus.OK
    assert resp.json['ok']
    assert resp.json['data'] is None


def test_list_size_one_after_post_company_data(client):
    resp = client.post('/company_data/', data=json.dumps({
        'quantity_of_employees': '200',
        'address': 'Ing Enrique Butty 275, C1001AFA CABA',
        'capabilities': 'Blockchain',
        'mission': "to lead in the creation, development and manufacture of "
                   "the industry's most advanced information technologies, "
                   "including computer systems, software, networking systems, "
                   "storage devices and microelectronics.",
        'vision': "to be the world’s most successful and important information"
                  "technology company.",
        'values': "Dedication to every client's success."
                  "Innovation that matters, for our company and for the world."
                  "Trust and personal responsibility in all relationships."
    }), content_type='application/json')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.CREATED
    resp = client.get('/company_data/')
    assert len(resp.json['data']) == 1
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.OK


def test_get_company_data_with_unmatched_query(client):
    resp = client.post('/company_data/', data=json.dumps({
        'quantity_of_employees': '200',
        'address': 'Ing Enrique Butty 275, C1001AFA CABA',
        'capabilities': 'Blockchain',
        'mission': "to lead in the creation, development and manufacture of "
                   "the industry's most advanced information technologies, "
                   "including computer systems, software, networking systems, "
                   "storage devices and microelectronics.",
        'vision': "to be the world’s most successful and important information"
                  "technology company.",
        'values': "Dedication to every client's success."
                  "Innovation that matters, for our company and for the world."
                  "Trust and personal responsibility in all relationships."
    }), content_type='application/json')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.CREATED
    resp = client.get('/company_data/?quantity_of_employees=201')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.OK
    assert len(resp.json['data']) == 0


def test_get_company_data_with_good_query(client):
    resp = client.post('/company_data/', data=json.dumps({
        'quantity_of_employees': '200',
        'address': 'Ing Enrique Butty 275, C1001AFA CABA',
        'capabilities': 'Blockchain',
        'mission': "to lead in the creation, development and manufacture of "
                   "the industry's most advanced information technologies, "
                   "including computer systems, software, networking systems, "
                   "storage devices and microelectronics.",
        'vision': "to be the world’s most successful and important information"
                  "technology company.",
        'values': "Dedication to every client's success."
                  "Innovation that matters, for our company and for the world."
                  "Trust and personal responsibility in all relationships."
    }), content_type='application/json')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.CREATED
    resp = client.get('/company_data/?quantity_of_employees=200')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.OK
    assert len(resp.json['data']) == 1


def test_post_company_data_with_no_vision(client):
    resp = client.post('/company_data/', data=json.dumps({
        'quantity_of_employees': '200',
        'address': 'Ing Enrique Butty 275, C1001AFA CABA',
        'capabilities': 'Blockchain',
        'mission': "to lead in the creation, development and manufacture of "
                   "the industry's most advanced information technologies, "
                   "including computer systems, software, networking systems, "
                   "storage devices and microelectronics.",
        'values': "Dedication to every client's success."
                  "Innovation that matters, for our company and for the world."
                  "Trust and personal responsibility in all relationships."
    }), content_type='application/json')
    assert not resp.json['ok']
    assert resp.status_code == HTTPStatus.BAD_REQUEST


def test_post_company_data_with_mission_invalid_type(client):
    resp = client.post('/company_data/', data=json.dumps({
        'quantity_of_employees': '200',
        'address': 'Ing Enrique Butty 275, C1001AFA CABA',
        'capabilities': 'Blockchain',
        'mission': 32,
        'vision': "to be the world’s most successful and important information"
                  "technology company.",
        'values': "Dedication to every client's success."
                  "Innovation that matters, for our company and for the world."
                  "Trust and personal responsibility in all relationships."
    }), content_type='application/json')
    assert not resp.json['ok']
    assert resp.status_code == HTTPStatus.BAD_REQUEST


def test_deleting_posted_company_data(client):
    resp = client.post('/company_data/', data=json.dumps({
        'quantity_of_employees': '200',
        'address': 'Ing Enrique Butty 275, C1001AFA CABA',
        'capabilities': 'Blockchain',
        'mission': "to lead in the creation, development and manufacture of "
                   "the industry's most advanced information technologies, "
                   "including computer systems, software, networking systems, "
                   "storage devices and microelectronics.",
        'vision': "to be the world’s most successful and important information"
                  "technology company.",
        'values': "Dedication to every client's success."
                  "Innovation that matters, for our company and for the world."
                  "Trust and personal responsibility in all relationships."
    }), content_type='application/json')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.CREATED
    _id = resp.json['data']
    resp = client.delete('/company_data/' + _id + '/')
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.OK


def test_deleting_not_existent_company_data(client):
    bad_id = 'fafafafafafafafafafafafa'  # fake mongo 24-char hex string
    resp = client.delete('/company_data/' + bad_id + '/')
    assert not resp.json['ok']
    assert resp.status_code == HTTPStatus.BAD_REQUEST


def test_delete_company_data_invalid_id(client):
    bad_id = "not hex wrong len"
    resp = client.delete(f'/company_data/{bad_id}/')
    assert resp.status_code == HTTPStatus.BAD_REQUEST


def test_updating_company_data(client):
    post_resp = client.post('/company_data/', data=json.dumps({
        'quantity_of_employees': '200',
        'address': 'Ing Enrique Butty 275, C1001AFA CABA',
        'capabilities': 'Blockchain',
        'mission': "to lead in the creation, development and manufacture of "
                   "the industry's most advanced information technologies, "
                   "including computer systems, software, networking systems, "
                   "storage devices and microelectronics.",
        'vision': "to be the world’s most successful and important information"
                  "technology company.",
        'values': "Dedication to every client's success."
                  "Innovation that matters, for our company and for the world."
                  "Trust and personal responsibility in all relationships."
    }), content_type='application/json')
    assert post_resp.json['ok']
    assert post_resp.status_code == HTTPStatus.CREATED
    _id = post_resp.json['data']

    patch_resp = client.patch('/company_data/', data=json.dumps({
        '_id': _id,
        'address': 'unknown',
    }), content_type='application/json')
    assert patch_resp.json['ok']
    assert patch_resp.status_code == HTTPStatus.CREATED
    assert patch_resp.json['data'] == _id

    get_resp = client.get('/company_data/')
    assert get_resp.json['ok']
    assert get_resp.status_code == HTTPStatus.OK
    assert get_resp.json['data'][0]['address'] == 'unknown'


def test_get_company_data_without_logging_in(auth_client):
    resp = auth_client.get('/company_data/')
    assert resp.status_code == HTTPStatus.UNAUTHORIZED
    assert not resp.json['ok']


def test_post_company_data_with_missing_arguments(client):
    post_resp = client.post('/company_data/', data=json.dumps({
        'address': 'Ing Enrique Butty 275, C1001AFA CABA',
        'capabilities': 'Blockchain',
        'mission': "to lead in the creation, development and manufacture of "
                   "the industry's most advanced information technologies, "
                   "including computer systems, software, networking systems, "
                   "storage devices and microelectronics.",
        'vision': "to be the world’s most successful and important information"
                  "technology company.",
        'values': "Dedication to every client's success."
                  "Innovation that matters, for our company and for the world."
                  "Trust and personal responsibility in all relationships."
    }), content_type='application/json')
    assert not post_resp.json['ok']
    assert post_resp.status_code == HTTPStatus.BAD_REQUEST


def test_update_company_data_with_the_same_data(client):
    post_resp = client.post('/company_data/', data=json.dumps({
        'quantity_of_employees': '200',
        'address': 'Ing Enrique Butty 275, C1001AFA CABA',
        'capabilities': 'Blockchain',
        'mission': "to lead in the creation, development and manufacture of "
                   "the industry's most advanced information technologies, "
                   "including computer systems, software, networking systems, "
                   "storage devices and microelectronics.",
        'vision': "to be the world’s most successful and important information"
                  "technology company.",
        'values': "Dedication to every client's success."
                  "Innovation that matters, for our company and for the world."
                  "Trust and personal responsibility in all relationships."
    }), content_type='application/json')
    assert post_resp.json['ok']
    assert post_resp.status_code == HTTPStatus.CREATED
    _id = post_resp.json['data']

    patch_resp = client.post('/company_data/', data=json.dumps({
        '_id': _id,
        'quantity_of_employees': '200',
        'address': 'Ing Enrique Butty 275, C1001AFA CABA',
        'capabilities': 'Blockchain',
        'mission': "to lead in the creation, development and manufacture of "
                   "the industry's most advanced information technologies, "
                   "including computer systems, software, networking systems, "
                   "storage devices and microelectronics.",
        'vision': "to be the world’s most successful and important information"
                  "technology company.",
        'values': "Dedication to every client's success."
                  "Innovation that matters, for our company and for the world."
                  "Trust and personal responsibility in all relationships."
    }), content_type='application/json')
    assert patch_resp.json['ok']
    assert patch_resp.status_code == HTTPStatus.CREATED


def test_get_company_data_with_query(client):
    quantity_of_employees = '200'
    address = 'Ing Enrique Butty 275, C1001AFA CABA'
    post_resp = client.post('/company_data/', data=json.dumps({
        'quantity_of_employees': quantity_of_employees,
        'address': address,
        'capabilities': 'Blockchain',
        'mission': "to lead in the creation, development and manufacture of "
                   "the industry's most advanced information technologies, "
                   "including computer systems, software, networking systems, "
                   "storage devices and microelectronics.",
        'vision': "to be the world’s most successful and important information"
                  "technology company.",
        'values': "Dedication to every client's success."
                  "Innovation that matters, for our company and for the world."
                  "Trust and personal responsibility in all relationships."
    }), content_type='application/json')
    assert post_resp.json['ok']
    assert post_resp.status_code == HTTPStatus.CREATED

    query = f"/users/?quantity_of_employees={quantity_of_employees}" \
        f"&address={address}"
    get_resp = client.get(query)
    assert get_resp.json['ok']
    assert get_resp.status_code == HTTPStatus.OK


def test_client_post_company_data_is_not_allowed(auth_client):
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

    resp = auth_client.post('/company_data/', data=json.dumps({
        'quantity_of_employees': '200',
        'address': 'Ing Enrique Butty 275, C1001AFA CABA',
        'capabilities': 'Blockchain',
        'mission': "to lead in the creation, development and manufacture of "
                   "the industry's most advanced information technologies, "
                   "including computer systems, software, networking systems, "
                   "storage devices and microelectronics.",
        'vision': "to be the world’s most successful and important information"
                  "technology company.",
        'values': "Dedication to every client's success."
                  "Innovation that matters, for our company and for the world."
                  "Trust and personal responsibility in all relationships."
    }),
        content_type='application/json',
        headers={'Authorization': 'Bearer ' + token})
    assert not resp.json['ok']
    assert resp.status_code == HTTPStatus.UNAUTHORIZED


def test_admin_post_company_data_is_allowed(auth_client):
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

    resp = auth_client.post('/company_data/', data=json.dumps({
        'quantity_of_employees': '200',
        'address': 'Ing Enrique Butty 275, C1001AFA CABA',
        'capabilities': 'Blockchain',
        'mission': "to lead in the creation, development and manufacture of "
                   "the industry's most advanced information technologies, "
                   "including computer systems, software, networking systems, "
                   "storage devices and microelectronics.",
        'vision': "to be the world’s most successful and important information"
                  "technology company.",
        'values': "Dedication to every client's success."
                  "Innovation that matters, for our company and for the world."
                  "Trust and personal responsibility in all relationships."
    }),
        content_type='application/json',
        headers={'Authorization': 'Bearer ' + token})
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.CREATED
