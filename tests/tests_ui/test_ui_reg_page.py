import time
from tests.base_ui import BaseCase
from ui.fixtures import *


class TestUIRegPage(BaseCase):

    @pytest.mark.UI
    def test_create_account(self):
        date = self.base_page.form_valid_user_data()
        self.base_page.get_create_account_page()

        self.reg_page.create_account(**date)
        time.sleep(3)
        assert f'{self.url}/welcome/' == self.driver.current_url

    @pytest.mark.UI
    def test_invalid_name_creation(self):
        data = {"username": "1", "password": "pass", "email": "invalid_name@mil.ru"}
        self.base_page.get_create_account_page()

        self.reg_page.create_account(**data)

        assert self.base_page.find(self.reg_page.locators.INVALID_NAME_DIV).is_displayed()

    @pytest.mark.UI
    def test_invalid_password_creation(self):
        data = {"username": "valid_name", "password": "pass", "email": "invalid_pas@mil.ru"}
        self.base_page.get_create_account_page()

        self.reg_page.create_account(**data, password_repeated="new_pas")

        assert self.base_page.find(self.reg_page.locators.INVALID_PASSWORD_MATCH, timeout=3).is_displayed()

    @pytest.mark.UI
    def test_invalid_email_creation(self):
        data = {"username": "valid_name", "password": "pass", "email": "invalid_email"}
        self.base_page.get_create_account_page()

        self.reg_page.create_account(**data)

        assert self.base_page.find(self.reg_page.locators.INVALID_EMAIL_DIV, timeout=3).is_displayed()

    @pytest.mark.UI     #---
    def test_exist_email_creation(self):
        data = {"username": "name_exict_mail", "password": "pass", "email": "valentina@mail.ru"}
        self.base_page.get_create_account_page()

        self.reg_page.create_account(**data)

        assert (self.base_page.find(self.reg_page.locators.INVALID_EXIST_USER_DIV, timeout=3).is_displayed() or
                self.base_page.find(self.reg_page.locators.INVALID_EMAIL_DIV, timeout=3).is_displayed())

    @pytest.mark.UI
    def test_exist_user_creation(self):
        data = {"username": "valentina", "password": "pass", "email": "new_mail@mail.ru"}
        self.base_page.get_create_account_page()

        self.reg_page.create_account(**data)

        assert self.base_page.find(self.reg_page.locators.INVALID_EXIST_USER_DIV, timeout=3).is_displayed()

    @pytest.mark.UI     #---
    def test_invalid_data_creation(self):
        data = {"username": "invalid_very_large_data", "password": "pass", "email": "invalid_email"}
        self.base_page.get_create_account_page()
        self.reg_page.create_account(**data)
        time.sleep(3)

        assert (self.base_page.find(self.reg_page.locators.INVALID_NAME_DIV, timeout=3).is_displayed() or
                self.base_page.find(self.reg_page.locators.INVALID_EMAIL_DIV, timeout=3).is_displayed())
