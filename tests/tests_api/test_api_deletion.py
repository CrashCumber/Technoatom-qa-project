import json
from faker import Faker
from tests.base_api import BaseCase
import pytest


class TestAPIDeletion(BaseCase):

    @pytest.mark.API #+++
    def test_delete_user_status_code(self, api_client):
        data = api_client.form_valid_user_data(have_access=True)

        api_client.insert_user_in_db(data)

        response = api_client.delete(data["username"])
        assert response.status_code == 204,  "Response status code isn't 204"

    @pytest.mark.API #+++
    def test_delete_user_from_db(self, api_client):
        data = api_client.form_valid_user_data(have_access=True)
        api_client.insert_user_in_db(data)

        api_client.delete(data["username"])

        response_db = api_client.get_user_from_db(data["username"])
        response_data = json.loads(response_db.text)
        assert response_data == "0"

    @pytest.mark.API #+++
    def test_delete_nonexistent_user_status_code(self, api_client):
        username = "nonexistent"

        response = api_client.delete(username)
        assert response.status_code == 404

        response_db = api_client.get_user_from_db(username)
        response_data = int(json.loads(response_db.text))
        assert response_data == 0

    @pytest.mark.API  # +++
    def test_delete_nonexistent_data_in_db(self, api_client):
        username = "nonexistent"

        api_client.delete(username)

        response_db = api_client.get_user_from_db(username)
        response_data = int(json.loads(response_db.text))
        assert response_data == 0
