import pytest
from mongoengine import connect, disconnect

@pytest.fixture
def test_app():
    from app import app

    return app

@pytest.fixture
def client(test_app):
    return test_app.test_client()
    
@pytest.fixture(scope="function")
def database(test_app):
    with test_app.app_context():
        disconnect()
        connect('mongoenginetest', host='mongomock://localhost/mocking_db')