import time
import allure
from tests.base_api import BaseCase
import pytest


class DataInvalid:
    data1 = {"username": 'invalid_email', "password": "invalid_email", "email": "invalid_email"}
    data2 = {"username": 'zero_email', "password": "zero_email", "email": ""}
    data3 = {"username": 'invalid_pas', "password": "", "email": "invalid_passowd@mail.ru"}
    data4 = {"username": 'very_big_length_username', "password": "big_length_username_pas", "email": "big_length_username@mail.ru"}
    data5 = {"username": '', "password": "zero_length_username_pass", "email": "zero_length_username@mail.ru"}
    data6 = {"username": 's', "password": "small_length_username_pas", "email": "small_length_username@mail.ru"}


class DataExist:
    data1 = {"username": 'valentina', "password": "valentina", "email": "valentina@mail.ru"}
    data2 = {"username": 'valentina', "password": "new_pas", "email": "valentina@mail.ru"}
    data3 = {"username": 'valentina', "password": "valentina", "email": "new_mail@mail.ru"}
    data4 = {"username": 'valentina', "password": "new_pas", "email": "new_mail@mail.ru"}


@pytest.mark.API
class TestAPICreation(BaseCase):

    @allure.title("Проверка кода ответа сервера при создании аккаунта")
    @pytest.mark.API_CREATION
    def test_create_account_status_code(self, api_client, user_without_access_field):
        """Проверка кода ответа сервера при создании аккаунта.
        Запрос по урлу /api/add_user с валидными данными пользователя.
        Ответ сервера должен быть 201.
        """

        data = user_without_access_field
        response = api_client.create(data["username"], data["password"], data["email"])
        assert response.status_code == 201, "Статус ответа отличный от 201"

    @allure.title("Проверка сохраненных данных при создании аккаунта")
    @pytest.mark.API_CREATION
    def test_create_account_save_in_db(self, api_client, user_without_access_field):
        """Проверка данных пользователя в базе данных при создании аккаунта.
        Запрос по урлу /api/add_user с валидными данными пользователя.
        Данные должны быть сохранены, access - 1.
        """

        data = user_without_access_field
        api_client.create(data["username"], data["password"], data["email"])

        response_data = api_client.get_user_from_db(data["username"])
        time.sleep(1)
        assert response_data["username"] == data["username"]
        assert response_data["password"] == data["password"]
        assert response_data["email"] == data["email"]
        assert response_data["access"] == 1

    @allure.title("Проверка кода ответа сервера при создании аккаунта с существующими именем пользователя")
    @pytest.mark.API_CREATION
    @pytest.mark.parametrize("data", [DataExist.data1, DataExist.data2, DataExist.data3, DataExist.data4])
    def test_existent_user(self, api_client, data):
        """Проверка кода ответа сервера при создании аккаунта с существующими именем пользователя.
        Запрос по урлу /api/add_user с невалидными именем пользователя.
        Ответ сервера должен быть 304.
        """

        response = api_client.create(**data)
        assert response.status_code == 304, 'Статус ответа отличный от 304'

    @allure.title("Проверка создания аккаунта с невалидными данными")
    @pytest.mark.API_CREATION
    @pytest.mark.parametrize("data", [DataInvalid.data1, DataInvalid.data2, DataInvalid.data3, DataInvalid.data4, DataInvalid.data5, DataInvalid.data6])
    def test_invalid_data(self, api_client, data):
        """Проверка создания аккаунта с невалидными данными.
        Запрос по урлу /api/add_user с невалидными данными пользователя, проверка данных в базе.
        Данные по пользователю в бд должны отсутствовать(пользователь не создан).
        """

        api_client.create(**data)
        response_data = api_client.get_user_from_db(data["username"])
        api_client.delete_user_from_db(data["username"])

        assert response_data == None, 'Невалидные данные сохранены в базу, пользователь создан'

    @allure.title("Проверка кода ответа сервера при создании аккаунта с невалидными данными")
    @pytest.mark.API_CREATION
    def test_invalid_data_status(self, api_client, data=DataInvalid.data1):
        """Проверка кода ответа сервера при создании аккаунта с невалидными данными.
        Запрос по урлу /api/add_user с невалидными данными пользователя.
        Ответ сервера должен быть 400(невалидные данных- плохой запрос).
        """

        response = api_client.create(**data)
        api_client.delete_user_from_db(data["username"])

        assert response.status_code == 400, 'Статус ответа отличный от 400'


