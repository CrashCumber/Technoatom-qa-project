import json

import allure

from tests.base_api import BaseCase
import pytest


class TestAPIActivation(BaseCase):

    @allure.title("Проверка статуса пользователя при авторизации")
    @pytest.mark.API_ACTION
    def test_auto_status_active(self, api_client, user_with_access):
        """Проверка статуса пользователя при авторизации.
        Запрос по урлу /login/ с валидными существующими данными пользователя.
        Статус active должен стать 1.
        """
        data = user_with_access

        api_client.authorization(data["username"], data["password"])

        response_data = api_client.get_user_from_db(data["username"])

        assert response_data["active"] == 1, response_data

    @allure.title("Проверка кода ответа сервера при деавторизации")
    @pytest.mark.API_ACTION
    def test_logout_status_code(self, api_client, user_with_access):
        """Проверка кода ответа сервера при деавторизации.
        Деавторизация пользователя.
        Ответ сервера должен быть успешный 200.
        """

        data = user_with_access

        api_client.active_user(data["username"])

        response = api_client.logout()
        assert response.status_code == 200, response.status_code

    @allure.title("Проверка данных пользователя после деавторизации")
    @pytest.mark.API_ACTION #-----!
    def test_logout_data_in_db(self, api_client, user_with_access):
        """Проверка данных пользователя после деавторизации.
        Деавторизация пользователя.
        Статус active должен стать 0.
        """

        data = user_with_access
        api_client.active_user(data["username"])

        api_client.logout()

        response_data = api_client.get_user_from_db(data["username"])

        assert response_data["active"] == 0, response_data
        assert response_data["access"] == 1, response_data
        assert response_data["password"] == data["password"], response_data

    @allure.title("Проверка статуса приложения")
    @pytest.mark.API_ACTION
    def test_app_ready(self, api_client):
        """Проверка статуса приложения.
        Запрос по урлу /status.
        Ответ с сервера со статусом приложения "ok".
        """

        response = api_client.status()
        assert response.status_code == 200, response.status_code

        response = json.loads(response.text)
        assert "ok" in response["status"], response


 # @pytest.mark.API
    # def test_auto_time(self, api_client):
    #     data = api_client.form_valid_user_data(have_access=True)
    #     api_client.insert_user_in_db(data)
    #
    #     api_client.authorization(data["username"], data["password"])
    #     time = datetime.datetime.now()
    #     time = time.strftime('%Y-%d-%m %H:%M:%S')
    #
    #     response_db = api_client.get_user_from_db(data["username"])
    #     response_data = json.loads(response_db.text)
    #
    #     assert response_data["start_active_time"] == time, f'{response_data["start_active_time"]}, {time}'
    #
    #     api_client.delete_user_from_db(data["username"])
