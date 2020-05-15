import datetime
import json
import time
from faker import Faker
from base_api import BaseCase
import pytest
fake = Faker()


class TestAPIActivation(BaseCase):

    @pytest.mark.API
    def test_auto_status_active(self, api_client):
        data = api_client.form_valid_user_data(have_access=True)
        api_client.insert_user_in_db(data)

        api_client.authorization(data["username"], data["password"])

        response_db = api_client.get_user_from_db(data["username"])
        response_data = json.loads(response_db.text)

        assert response_data["active"] == 1

        api_client.delete_user_from_db(data["username"])

    @pytest.mark.API
    def test_auto_time(self, api_client):
        data = api_client.form_valid_user_data(have_access=True)
        api_client.insert_user_in_db(data)

        api_client.authorization(data["username"], data["password"])
        time = datetime.datetime.now()
        time = time.strftime('%Y-%d-%m %H:%M:%S')

        response_db = api_client.get_user_from_db(data["username"])
        response_data = json.loads(response_db.text)

        assert response_data["start_active_time"] == time, f'{response_data["start_active_time"]}, {time}'

        api_client.delete_user_from_db(data["username"])

    @pytest.mark.API
    def test_logout_status_code(self, api_client):
        data = api_client.form_valid_user_data(have_access=True)
        api_client.insert_user_in_db(data)
        api_client.active_user(data["username"])

        response = api_client.logout()
        assert response.status_code == 200

        api_client.delete_user_from_db(data["username"])

    @pytest.mark.API
    def test_logout_data_in_db(self, api_client):
        data = api_client.form_valid_user_data(have_access=True)
        api_client.insert_user_in_db(data)
        api_client.active_user(data["username"])

        api_client.logout()

        response_db = api_client.get_user_from_db(data["username"])
        response_data = json.loads(response_db.text)

        assert response_data["active"] == 0
        assert response_data["access"] == 1
        assert response_data["password"] == data["password"]

        api_client.delete_user_from_db(data["username"])

    @pytest.mark.API #+++
    def test_app_ready(self, api_client):
        response = api_client.status()
        assert response.status_code == 200
        response = json.loads(response.text)
        assert "ok" in response["status"]
