import json
from faker import Faker
from base_api import BaseCase
import pytest
from api.api_client import URLS

fake = Faker()


class TestAPIDeletion(BaseCase):

    @pytest.mark.skip(reason='TEMP')
    @pytest.mark.API
    def test_delete_user(self, api_client):
        data = api_client.form_valid_user_data(have_access=True)

        api_client.insert_usr_in_db(data)

        response = api_client.delete(data["username"])
        assert response.status_code == 204,  "Response status code isn't 204"

        response_db = api_client.get_user_from_db(data["username"])
        response_data = int(json.loads(response_db.text))
        assert response_data == 0

    @pytest.mark.skip(reason='TEMP')
    @pytest.mark.API
    def test_delete_nonexistent_user(self, api_client):
        username = "nonexistent"

        response = api_client.delete(username)
        assert response.status_code == 404

        response_db = api_client.get_user_from_db(username)
        response_data = int(json.loads(response_db.text))
        assert response_data == 0
