import time
from tests.base_ui import BaseCase
from ui.fixtures import *


@pytest.mark.UI
class TestUIRegPage(BaseCase):

    @allure.title("Создание аккаунта")
    @pytest.mark.UI_REG
    def test_create_account(self, user_without_access_field):
        """Создание аккаунта с валидными данными.
        Ввод данных в поля регистрации.
        Переход на главную страницу
        """

        date = user_without_access_field
        self.base_page.get_create_account_page()

        self.reg_page.create_account(**date)
        time.sleep(3)
        assert f'{self.url}/welcome/' == self.driver.current_url

    @allure.title("Создание аккаунта с невалидным именем(коротким)")
    @pytest.mark.UI_REG
    def test_invalid_name_creation(self):
        """Создание аккаунта с невалидным коротким именем.
        Ввод данных в поля регистрации.
        Появление окна с описанием невалидности введенных данных.
        """

        data = {"username": "1", "password": "pass", "email": "invalid_name@mil.ru"}
        self.base_page.get_create_account_page()

        self.reg_page.create_account(**data)

        assert self.base_page.find(self.reg_page.locators.INVALID_NAME_DIV).is_displayed()

    @allure.title("Создание аккаунта с невалидным подтверждением пароля")
    @pytest.mark.UI_REG
    def test_invalid_password_creation(self):
        """Создание аккаунта с невалидным подтверждением пароля.
        Ввод данных в поля регистрации.
        Появление окна с описанием невалидности введенных данных.
        """

        data = {"username": "valid_name", "password": "pass", "email": "invalid_pas@mil.ru"}
        self.base_page.get_create_account_page()

        self.reg_page.create_account(**data, password_repeated="new_pas")

        assert self.base_page.find(self.reg_page.locators.INVALID_PASSWORD_MATCH, timeout=2).is_displayed()

    @allure.title("Создание аккаунта с невалидной почтой")
    @pytest.mark.UI_REG
    def test_invalid_email_creation(self):
        """Создание аккаунта с невалидной почтой.
        Ввод данных в поля регистрации.
        Появление окна с описанием невалидности введенных данных.
        """

        data = {"username": "valid_name", "password": "pass", "email": "invalid_email"}
        self.base_page.get_create_account_page()

        self.reg_page.create_account(**data)

        assert self.base_page.find(self.reg_page.locators.INVALID_EMAIL_DIV, timeout=2).is_displayed()

    @allure.title("Создание аккаунта с существующей почтой")
    @pytest.mark.UI_REG
    def test_exist_email_creation(self):
        """Создание аккаунта с зарегестрированного почтой.
        Ввод данных в поля регистрации.
        Появление окна с описанием невалидности введенных данных.
        """

        data = {"username": "name_exict_mail", "password": "pass", "email": "valentina@mail.ru"}
        self.base_page.get_create_account_page()

        self.reg_page.create_account(**data)

        assert (self.base_page.find(self.reg_page.locators.INVALID_EXIST_USER_DIV, timeout=2).is_displayed() or
                self.base_page.find(self.reg_page.locators.INVALID_EMAIL_DIV, timeout=2).is_displayed())

    @allure.title("Создание аккаунта с существующим именем")
    @pytest.mark.UI_REG
    def test_exist_user_creation(self):
        """Создание аккаунта с именем зарегестрированного пользователя.
        Ввод данных в поля регистрации.
        Появление окна с описанием невалидности введенных данных.
        """

        data = {"username": "valentina", "password": "pass", "email": "new_mail@mail.ru"}
        self.base_page.get_create_account_page()

        self.reg_page.create_account(**data)

        assert self.base_page.find(self.reg_page.locators.INVALID_EXIST_USER_DIV, timeout=2).is_displayed()

    @allure.title("Создание аккаунта с невалидным именем (большим)")
    @pytest.mark.UI_REG
    def test_invalid_data_creation(self):
        """Создание аккаунта с невалидным длинным именем.
        Ввод данных в поля регистрации.
        Появление окна с описанием невалидности введенных данных.
        """

        data = {"username": "invalid_very_large_data", "password": "pass", "email": "invalid_email"}
        self.base_page.get_create_account_page()
        self.reg_page.create_account(**data)

        assert (self.base_page.find(self.reg_page.locators.INVALID_NAME_DIV, timeout=2).is_displayed() or
                self.base_page.find(self.reg_page.locators.INVALID_EMAIL_DIV, timeout=2).is_displayed())
