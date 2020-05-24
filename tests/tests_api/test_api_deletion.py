import allure
from tests.base_api import BaseCase
import pytest


class TestAPIDeletion(BaseCase):

    @allure.title("Проверка кода ответа при удалении пользователя")
    @pytest.mark.API_DELETION
    def test_delete_user_status_code(self, api_client, user_data):
        """Проверка кода ответа при удалении пользователя.
        Запрос по урлу /api/del_user/<username> с именем пользователя.
        Код ответа должен быть 204(сущность удалена).
        """

        data = user_data

        response = api_client.delete(data["username"])
        assert response.status_code == 204,  response.status_code

    @allure.title("Проверка данных в базе при удалении пользователя")
    @pytest.mark.API_DELETION
    def test_delete_user_from_db(self, api_client, user_data):
        """Проверка данных в базе при удалении пользователя.
        Запрос по урлу /api/del_user/<username> с именем пользователя.
        Данные из базы должны быть удалены.
        """

        data = user_data
        api_client.delete(data["username"])

        response_data = api_client.get_user_from_db(data["username"])

        assert response_data is None, response_data

    @allure.title("Проверка кода ответа при невалидном удалении пользователя(несуществующем)")
    @pytest.mark.API_DELETION
    def test_delete_nonexistent_user_status_code(self, api_client):
        """Проверка кода ответа при удалении несуществующего пользователя.
        Запрос по урлу /api/del_user/<username> с именем пользователя.
        Код ответа должен быть 404(сущности не существует).
        """

        username = "nonexistent"

        response = api_client.delete(username)
        assert response.status_code == 404, response.status_code

    @allure.title("Проверка данных в базе при удалении невуществующего пользователя")
    @pytest.mark.API_DELETION
    def test_delete_nonexistent_data_in_db(self, api_client):
        """Проверка отсутствие данных в базе при удалении несущестсвующего пользователя.
        Запрос по урлу /api/del_user/<username> с именем пользователя.
        Данные должны отсутствовать.
        """

        username = "nonexistent"

        api_client.delete(username)

        response_data = api_client.get_user_from_db(username)
        assert response_data is None, response_data
