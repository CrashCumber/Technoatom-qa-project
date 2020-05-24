import allure

from tests.base_api import BaseCase
import pytest


class TestAPIBlockage(BaseCase):

    @allure.title("Проверка кода ответа при блокировке пользователя")
    @pytest.mark.API_BLOCK
    def test_block_user_status_code(self, api_client, user_with_access):
        """Проверка кода ответа при блокировке пользователя.
        Запрос по урлу /api/block_user/<username> с именем пользователя.
        Код ответа должен быть 200.
        """

        data = user_with_access
        response = api_client.block(data["username"])
        assert response.status_code == 200

    @allure.title("Проверка данных в базе при блокировке пользователя")
    @pytest.mark.API_BLOCK
    def test_block_user_data_in_db(self, api_client, user_with_access):
        """Проверка данных в базе при блокировке пользователя.
        Запрос по урлу /api/block_user/<username> с именем пользователя.
        Статус access должен быть 0.
        """

        data = user_with_access

        response_data = api_client.get_user_from_db(data["username"])
        assert response_data["access"] == 0, response_data

    @allure.title("Проверка кода ответа при разблокировке пользователя")
    @pytest.mark.API_BLOCK
    def test_unblock_user_status_code(self, api_client, user_with_zero_access):
        """Проверка кода ответа при разблокировке пользователя.
        Запрос по урлу /api/accept_user/<username> с именем пользователя.
        Код ответа должен быть 200.
        """

        data = user_with_zero_access
        response = api_client.unblock(data["username"])
        assert response.status_code == 200, response.status_code

    @allure.title("Проверка данных в базе при разблокировке пользователя")
    @pytest.mark.API_BLOCK
    def test_unblock_user_data_in_db(self, api_client, user_with_zero_access):
        """Проверка данных в базе при разблокировке пользователя.
        Запрос по урлу /api/accept_user/<username> с именем пользователя.
        Статус access должен быть 1.
        """

        data = user_with_zero_access
        api_client.unblock(data["username"])
        response_data = api_client.get_user_from_db(data["username"])
        assert response_data["access"] == 1, response_data

    @allure.title("Проверка кода ответа при блокировке несуществующего пользователя")
    @pytest.mark.API_BLOCK
    def test_block_nonexistent_user(self, api_client):
        """Блокировка несуществующего пользователя.
        Запрос по урлу /api/block_user/<username> с именем пользователя.
        Код ответа должен быть 404.
        """

        username = "nonexistent"

        response = api_client.block(username)
        assert response.status_code == 404, response.status_code

    @allure.title("Проверка кода ответа при разблокировке несуществующего пользователя")
    @pytest.mark.API_BLOCK
    def test_unblock_nonexistent_user(self, api_client):
        """Блокировка несуществующего пользователя.
        Запрос по урлу /api/accept_user/<username> с именем пользователя.
        Код ответа должен быть 404.
        """

        username = "nonexistent"

        response = api_client.unblock(username)
        assert response.status_code == 404, response.status_code

    @allure.title("Авторизация разлокирована пользователя")
    @pytest.mark.API_BLOCK
    def test_auto_block_user(self, api_client, user_with_zero_access):
        """Проверка возможности авторизации разлокированого пользователя.
        Запрос по урлу /login/ с валидными существующими данными пользователя.
        Код ответа должен быть 401(Пользователь не авторизован).
        """

        data = user_with_zero_access

        response = api_client.authorization(data["username"], data["password"])
        assert response.status_code == 401, response.status_code

    @allure.title("Блокировка пользователя во время пребывания на странице")
    @pytest.mark.API_BLOCK
    def test_block_while_active(self, api_client, user_with_access):
        """Блокировка пользователя во время пребывания на странице.
        Запрос по урлу /api/block_user/<username> с именем пользователя, у каоторого active = 1.
        Пользователь блокируется и деавторизируется access = 1 active = 0.
        """

        data = user_with_access
        api_client.active_user(data["username"])

        api_client.block(data["username"])

        response_data = api_client.get_user_from_db(data["username"])
        assert response_data["access"] == 0, response_data
        assert response_data["active"] == 0, response_data



