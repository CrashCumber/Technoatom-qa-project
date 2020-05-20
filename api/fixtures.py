import pytest
from api.api_client import ApiClient

@pytest.fixture(scope='function')
def user_with_access(api_client):
    data = api_client.form_valid_user_data(have_access=True)
    api_client.insert_user_in_db(data)
    yield data
    api_client.delete_user_from_db(data["username"])

@pytest.fixture(scope='function')
def user_with_zero_access(api_client):
    data = api_client.form_valid_user_data(have_access=True)
    api_client.insert_user_in_db(data)
    yield data
    api_client.delete_user_from_db(data["username"])

@pytest.fixture(scope='function')
def user_without_access(api_client):
    data = api_client.form_valid_user_data(have_access=True)
    api_client.insert_user_in_db(data)
    yield data
    api_client.delete_user_from_db(data["username"])

@pytest.fixture(scope='function')
def user_without_deletion(api_client):
    data = api_client.form_valid_user_data(have_access=True)
    api_client.insert_user_in_db(data)
    return data
