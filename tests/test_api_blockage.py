import json
from faker import Faker
from base_api import BaseCase
import pytest
from api.api_client import URLS
fake = Faker()


class TestAPIBlockage(BaseCase):

    @pytest.mark.API #+++
    def test_block_user_status_code(self, api_client):
        data = api_client.form_valid_user_data(have_access=True)
        api_client.insert_user_in_db(data)

        response = api_client.block(data["username"])
        assert response.status_code == 200

        api_client.delete_user_from_db(data["username"])

    @pytest.mark.API  # +++
    def test_block_user_data_in_db(self, api_client):
        data = api_client.form_valid_user_data(have_access=True)
        api_client.insert_user_in_db(data)

        response = api_client.block(data["username"])
        assert response.status_code == 200  # , "Response status code isn't 200"

        response_db = api_client.get_user_from_db(data["username"])
        response_data = json.loads(response_db.text)
        assert response_data["access"] == 0

        api_client.delete_user_from_db(data["username"])

    @pytest.mark.API#+++
    def test_unblock_user_status_code(self, api_client):
        data = api_client.form_valid_user_data(have_access=True, access_value=0)
        api_client.insert_user_in_db(data)

        response = api_client.unblock(data["username"])
        assert response.status_code == 200, "Response status code isn't 200"

        api_client.delete_user_from_db(data["username"])

    @pytest.mark.API  # +++
    def test_unblock_user_data_in_db(self, api_client):
        data = api_client.form_valid_user_data(have_access=True, access_value=0)
        api_client.insert_user_in_db(data)

        api_client.unblock(data["username"])

        response_db = api_client.get_user_from_db(data["username"])
        response_data = json.loads(response_db.text)
        assert response_data["access"] == 1, response_data

        api_client.delete_user_from_db(data["username"])

    @pytest.mark.API #+++
    def test_block_nonexistent_user(self, api_client):
        username = "nonexistent"

        response = api_client.block(username)
        assert response.status_code == 404

        response = api_client.unblock(username)
        assert response.status_code == 404

    @pytest.mark.API #+++
    def test_auto_block_user(self, api_client):
        data = api_client.form_valid_user_data(have_access=True, access_value=0)
        api_client.insert_user_in_db(data)

        response = api_client.authorization(data["username"], data["password"])
        assert response.status_code == 401

        api_client.delete_user_from_db(data["username"])

    @pytest.mark.API
    def test_block_while_active(self, api_client):
        data = api_client.form_valid_user_data(have_access=True)
        api_client.insert_user_in_db(data)

        api_client.authorization(data["username"], data["password"]) #change to active user def

        api_client.block(data["username"])

        response_db = api_client.get_user_from_db(data["username"])
        response_data = json.loads(response_db.text)
        assert response_data["access"] == 0, response_data
        assert response_data["active"] == 0, response_data

        api_client.delete_user_from_db(data["username"])


