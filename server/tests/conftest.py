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
    print("FIRST")


@pytest.fixture
def user_data():
    print("SECOND")
    data = {
        'first_name': fake.pystr(),
        'last_name': fake.pystr(),
        'user_name': fake.pystr(),
        'mail': fake.email(),
        'password': fake.password(),
        'dni': str(fake.random_number(8, True)),
        'type': fake.random_element(('client', 'admin'))
    }
    _id = UsersController.post(data)[0]['data']
    user_data = UsersController.get(_id)[0]['data']
    yield user_data
