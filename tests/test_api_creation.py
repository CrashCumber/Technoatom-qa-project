import json
import time
from faker import Faker
from base_api import BaseCase
import pytest

from api.api_client import URLS

fake = Faker()


class TestAPICreation(BaseCase):

    @pytest.mark.API
    def test_create_account_status_code(self, api_client):
        data = api_client.form_valid_user_data()
        response = api_client.create(data["username"], data["password"], data["email"])
        assert response.status_code == 201, "Response status code isn't 201"

        api_client.delete_user_from_db(data["username"])

    @pytest.mark.API #+++
    def test_create_account_save_in_db(self, api_client):
        data = api_client.form_valid_user_data()
        api_client.create(data["username"], data["password"], data["email"])

        response_db = api_client.get_user_from_db(data["username"])
        if response_db.status_code == 404:
            raise Exception(f'There isn`t the {data["username"]} in database')
        response_data = json.loads(response_db.text)
        time.sleep(1)
        assert response_data["username"] == data["username"]
        assert response_data["password"] == data["password"]
        assert response_data["email"] == data["email"]
        assert response_data["access"] == 1

        api_client.delete_user_from_db(data["username"])

    @pytest.mark.API #+++
    def test_existent_user(self, api_client):
        data = {"username": 'valentina', "password": "valentina", "email": "valentina@mail.ru"}

        response = api_client.create(**data)
        assert response.status_code == 304

        data = {"username": 'valentina', "password": "new_pas", "email": "valentina@mail.ru"}

        response = api_client.create(**data)
        assert response.status_code == 304

        data = {"username": 'valentina', "password": "valentina", "email": "new_mail@mail.ru"}

        response = api_client.create(**data)
        assert response.status_code == 304

        data = {"username": 'valentina', "password": "new_pas", "email": "new_mail@mail.ru"}

        response = api_client.create(**data)
        assert response.status_code == 304

    @pytest.mark.API
    def test_invalid_name_small_length(self, api_client):
        data = {"username": 's', "password": "small_length_username_pas", "email": "small_length_username@mail.ru"}

        response = api_client.create(**data)
        assert response.status_code == 400

    @pytest.mark.API
    def test_invalid_name_zero_length(self, api_client):
        data = {"username": '', "password": "zero_length_username_pass", "email": "zero_length_username@mail.ru"}

        response = api_client.create(**data)
        assert response.status_code == 400

    @pytest.mark.API
    def test_invalid_name_big_length(self, api_client):
        data = {"username": 'very_big_length_username', "password": "big_length_username_pas", "email": "big_length_username@mail.ru"}

        response = api_client.create(**data)
        assert response.status_code == 400

    @pytest.mark.API
    def test_invalid_password(self, api_client):
        data = {"username": 'invalid_pas', "password": "", "email": "invalid_passowd@mail.ru"}

        response = api_client.create(**data)
        assert response.status_code == 400

    @pytest.mark.API
    def test_invalid_email(self, api_client):
        data = {"username": 'invalid_email', "password": "invalid_email", "email": "invalid_email"}

        response = api_client.create(**data)
        assert response.status_code == 400

    @pytest.mark.API
    def test_invalid_zero_email(self, api_client):
        data = {"username": 'zero_email', "password": "zero_email", "email": ""}

        response = api_client.create(**data)
        assert response.status_code == 400


