import pytest
from faker import Faker
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
    yield client


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
