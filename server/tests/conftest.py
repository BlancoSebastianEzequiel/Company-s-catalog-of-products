import pytest
from faker import Faker

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
