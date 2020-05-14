import datetime
import json
from faker import Faker
from base_api import BaseCase
import pytest
from api.api_client import URLS
fake = Faker()


class TestAPIActivation(BaseCase):

    @pytest.mark.API
    def test_auto(self, api_client):
        data = api_client.form_valid_user_data(have_access=True)

        api_client.insert_usr_in_db(data)

        response = api_client.authorization(data["username"], data["password"])
        time = datetime.datetime.now()
        assert response.status_code == 200
        assert response.url == URLS.USER_PAGE

        response_db = api_client.get_user_from_db(data["username"])
        response_data = json.loads(response_db.text)
        assert response_data["active"] == 1
        assert response_data["start_active_time"] == time.strftime('%d-%m-%Y %H:%M:%S'), f'{response_data["start_active_time"]}, {time}'

        api_client.delete_user_from_db(data["username"])


    @pytest.mark.skip(reason='TEMP')
    @pytest.mark.API
    def test_logout(self, api_client):
        data = api_client.form_valid_user_data(have_access=True)

        api_client.insert_usr_in_db(data)

        api_client.authorization(data["username"], data["password"])
        time = datetime.datetime.now()

        response = api_client.logout()
        assert response.status_code == 200
        assert response.url == URLS.AUTORIZATION

        response_db = api_client.get_user_from_db(data["username"])
        response_data = json.loads(response_db.text)
        assert response_data["active"] == 0
        assert response_data["access"] == 1
        assert response_data["password"] == data["password"]
        assert response_data["start_active_time"] == time.strftime('%d-%m-%Y %H:%M:%S'),f'{response_data["start_active_time"]}, {time} '

        api_client.delete_user_from_db(data["username"])

    @pytest.mark.API
    def test_auto(self, api_client):
        data = api_client.form_valid_user_data(have_access=True)

        api_client.insert_usr_in_db(data)

        response = api_client.authorization(data["username"], data["password"])
        time = datetime.datetime.now()
        assert response.status_code == 200
        assert response.url == URLS.USER_PAGE

        response_db = api_client.get_user_from_db(data["username"])
        response_data = json.loads(response_db.text)
        assert response_data["active"] == 1
        assert response_data["start_active_time"] == time.strftime('%d-%m-%Y %H:%M:%S'), f'{response_data["start_active_time"]}, {time}'

        api_client.delete_user_from_db(data["username"])

 # @pytest.mark.skip(reason='TEMP')
 #    @pytest.mark.API
 #    def test_app_ready(self, api_client):
 #        response = api_client.status()
 #        assert response.status_code == 200
 #        response = json.loads(response.text)
 #        assert "ok" in response["status"]
