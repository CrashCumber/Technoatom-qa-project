import json
from faker import Faker
from base_api import BaseCase
import pytest
fake = Faker()

class TestAPI(BaseCase):

    # @pytest.mark.API
    # def test_auto(self, api_client):
    #     response = api_client.authorization('aleksandr', 'aleksandr_pas')
    #     assert response.status_code == 200

    @pytest.mark.skip(reason='TEMP')
    @pytest.mark.API
    def test_create_account(self, api_client):
        data = api_client.form_valid_user_data()

        response = api_client.create(data["username"], data["password"], data["email"])
        assert response.status_code == 201, "Response status code isn't 201(user was created)"

        response_db = api_client.get_user_from_db(data["username"])
        if response_db.status_code == 404:
            raise Exception(f'There isn`t the {data["username"]} in database')
        response_data = json.loads(response_db.text)
        assert response_data["username"] == data["username"], f'There isn`t the {data["username"]} in database'

    @pytest.mark.skip(reason='TEMP')
    @pytest.mark.API
    def test_delete_user(self, api_client):
        data = api_client.form_valid_user_data()

        api_client.create(data["username"], data["password"], data["email"])

        response_db = api_client.get_user_from_db(data["username"])
        if response_db.status_code == 404:
            raise Exception(f'There isn`t the {data["username"]} in database')
        response_data = json.loads(response_db.text)
        assert response_data["username"] == data["username"], f'There isn`t the {data["username"]} in database'

        response = api_client.delete(data["username"])
        assert response.status_code == 204,  "Response status code isn't 204(user was deleted)"

        response_db = api_client.get_user_from_db(data["username"])
        response_data = int(json.loads(response_db.text))
        assert response_data == 0


    #@pytest.mark.skip(reason='TEMP')
    @pytest.mark.API
    def test_block_user(self, api_client):
        data = api_client.form_valid_user_data()

        api_client.create(data["username"], data["password"], data["email"])

        response_db = api_client.get_user_from_db(data["username"])
        if response_db.status_code == 404:
            raise Exception(f'There isn`t the {data["username"]} in database')
        response_data = json.loads(response_db.text)
        assert response_data["username"] == data["username"], f'There isn`t the {data["username"]} in database'

        response = api_client.block(data["username"])
        assert response.status_code == 200, "Response status code isn't 200(action has done)"

        response_db = api_client.get_user_from_db(data["username"])
        response_data = json.loads(response_db.text)
        assert response_data["access"] == 0
        response = api_client.block(data["username"])
        assert response.status_code == 401 #"Response status code isn't 200(action has done)"

    @pytest.mark.skip(reason='TEMP')
    @pytest.mark.API
    def test_unblock_user(self, api_client):
        data = api_client.form_valid_user_data()

        api_client.create(data["username"], data["password"], data["email"])

        response_db = api_client.get_user_from_db(data["username"])
        if response_db.status_code == 404:
            raise Exception(f'There isn`t the {data["username"]} in database')
        response_data = json.loads(response_db.text)
        assert response_data["username"] == data["username"], f'There isn`t the {data["username"]} in database'

        response = api_client.block(data["username"])
        assert response.status_code == 200, "Response status code isn't 200(action has done)"

        response_db = api_client.get_user_from_db(data["username"])
        response_data = json.loads(response_db.text)
        assert response_data["access"] == 0

        response = api_client.unblock(data["username"])
        assert response.status_code == 200, "Response status code isn't 200(action has done)"

        response_db = api_client.get_user_from_db(data["username"])
        response_data = json.loads(response_db.text)
        assert response_data["access"] == 1
    @pytest.mark.skip(reason='TEMP')
    @pytest.mark.API
    def test_nonexistent_user(self, api_client):
        data = api_client.form_valid_user_data()
        response_db = api_client.get_user_from_db(data["username"])
        response_data = int(json.loads(response_db.text))
        assert response_data == 0

        response = api_client.block(data["username"])
        assert response.status_code == 404

        response = api_client.unblock(data["username"])
        assert response.status_code == 404

        response = api_client.delete(data["username"])
        assert response.status_code == 404


    @pytest.mark.skip(reason='TEMP')
    @pytest.mark.API
    def test_existent_user(self, api_client):
        data = {"username": 'valentina', "password": "valentina", "email": "valentina@mail.ru"}

        response = api_client.create(**data)
        assert response.status_code == 304

        data = {"username": 'valentina', "password": "1", "email": "valentina@mail.ru"}

        response = api_client.create(**data)
        assert response.status_code == 304

        data = {"username": 'valentina', "password": "valentina", "email": "111@mail.ru"}

        response = api_client.create(**data)
        assert response.status_code == 304
    @pytest.mark.skip(reason='TEMP')
    def test_invalid_request(self, api_client):
        data = {"username": '2', "password": "11111", "email": "11111@mail.ru"}

        response = api_client.create(**data)
        assert response.status_code == 400

        data = {"username": '111111111111111111111', "password": "11111", "email": "11111@mail.ru"}

        response = api_client.create(**data)
        assert response.status_code == 400

    @pytest.mark.skip(reason='TEMP')
    @pytest.mark.API
    def test_app_ready(self, api_client):
        response = api_client.status()
        assert response.status_code == 200
        response = json.loads(response.text)
        assert "ok" in response["status"]
