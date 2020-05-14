import json
from faker import Faker
from base_api import BaseCase
import pytest
from api.api_client import URLS
fake = Faker()


class TestAPIBlockage(BaseCase):

    @pytest.mark.skip(reason='TEMP')
    @pytest.mark.API
    def test_block_user(self, api_client):
        data = api_client.form_valid_user_data(have_access=True)

        api_client.insert_usr_in_db(data)

        response = api_client.block(data["username"])
        assert response.status_code == 200, "Response status code isn't 200"

        response_db = api_client.get_user_from_db(data["username"])
        response_data = json.loads(response_db.text)
        assert response_data["access"] == 0

        api_client.delete_user_from_db(data["username"])

    @pytest.mark.skip(reason='TEMP')
    @pytest.mark.API
    def test_unblock_user(self, api_client):
        data = api_client.form_valid_user_data(have_access=True, access_value=0)

        api_client.insert_user_in_db(data)

        response = api_client.unblock(data["username"])
        assert response.status_code == 200, "Response status code isn't 200"

        response_db = api_client.get_user_from_db(data["username"])
        response_data = json.loads(response_db.text)
        assert response_data["access"] == 1

        api_client.delete_user_from_db(data["username"])

    @pytest.mark.skip(reason='TEMP')
    @pytest.mark.API
    def test_block_nonexistent_user(self, api_client):
        username = "nonexistent"

        response = api_client.block(username)
        assert response.status_code == 404

        response = api_client.unblock(username)
        assert response.status_code == 404

    @pytest.mark.skip(reason='TEMP')
    @pytest.mark.API
    def test_auto_block_user(self, api_client):
        data = api_client.form_valid_user_data(have_access=True, access_value=0)

        api_client.insert_user_in_db(data)

        response = api_client.authorization(data["username"], data["password"])
        assert response.status_code == 401

        api_client.delete_user_from_db(data["username"])

    @pytest.mark.API
    def test_block_while_active(self, api_client):
        data = api_client.form_valid_user_data(have_access=True)

        api_client.insert_usr_in_db(data)

        api_client.authorization(data["username"], data["password"])

        response = api_client.block(data["username"])
        assert response.status_code == 200, "Response status code isn't 200"
        assert response.url == URLS.AUTORIZATION, f'{response.url}'
        assert response.url != URLS.USER_PAGE

        response_db = api_client.get_user_from_db(data["username"])
        response_data = json.loads(response_db.text)
        assert response_data["access"] == 0
        assert response_data["active"] == 0

        api_client.delete_user_from_db(data["username"])


