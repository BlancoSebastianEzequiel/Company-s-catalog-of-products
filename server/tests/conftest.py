import pytest
import json
from faker import Faker
from http import HTTPStatus
from server.controller.users import UsersController

from server.app import create_app
from server.libs.mongo import MONGO

fake = Faker()


@pytest.fixture
def client():
    app = create_app(conf='conf.test.Config')
    app.config['TESTING'] = True
    client = app.test_client()
    # Clear databases
    MONGO.db['users'].delete_many({})
    MONGO.db['active_principle'].delete_many({})
    MONGO.db['products'].delete_many({})
    yield client


@pytest.fixture
def auth_client():
    app = create_app(conf='conf.auth_test.Config')
    app.config['TESTING'] = True
    auth_client = app.test_client()
    # Clear databases
    MONGO.db['users'].delete_many({})
    MONGO.db['active_principle'].delete_many({})
    MONGO.db['products'].delete_many({})
    yield auth_client


@pytest.fixture
def random_user():
    secret = str(fake.random_number(8, True))
    name = fake.name()
    first_name = name.split(' ')[0]
    last_name = name.split(' ')[1]
    data = {
        'first_name': first_name,
        'last_name': last_name,
        'user_name': fake.pystr(),
        'email': fake.email(),
        'password': secret,
        'type': fake.random_element(('client', 'admin'))
    }
    _id = UsersController.post(data)[0]['data']
    user_data = UsersController.get(_id)[0]['data']
    yield user_data, secret


@pytest.fixture
def post_active_principle():
    app = create_app(conf='conf.test.Config')
    app.config['TESTING'] = True
    client = app.test_client()
    # Clear databases
    MONGO.db['users'].delete_many({})
    MONGO.db['active_principle'].delete_many({})
    MONGO.db['products'].delete_many({})

    active_principle_data = {
        'code': '200',
        'name': 'paracetamol',
        'description': 'analgésicos y antiinflamatorios'
    }
    resp = client.post(
        '/active_principle/',
        data=json.dumps(active_principle_data),
        content_type='application/json'
    )
    assert resp.json['ok']
    assert resp.status_code == HTTPStatus.CREATED
    active_principle_data['_id'] = resp.json['data']
    yield client, active_principle_data
