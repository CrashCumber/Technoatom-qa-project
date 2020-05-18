import time
import pytest
import selenium
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from tests.base_ui import BaseCase
from ui.fixtures import *


class TestUIBasePage(BaseCase):

    @pytest.mark.UI
    def test_existent_user_authorization(self):
        user = self.base_page.user
        password = self.base_page.password
        self.base_page.authorization(user, password)
        assert f'{self.url}/welcome/' == self.driver.current_url

    @pytest.mark.UI
    def test_invalid_length_username_authorization(self):
        user = 'invalid_very_big_username'
        password = 'valid_pass'
        self.base_page.authorization(user, password)

        assert self.base_page.find(self.base_page.locators.INVALID_USERNAME_LENGTH_DIV).is_displayed()
        assert f'{self.url}/login' == self.driver.current_url

    @pytest.mark.UI
    def test_nonexistent_user_authorization(self):
        user = 'nonexistent'
        password = 'nonexistent_pass'
        self.base_page.authorization(user, password)

        assert self.base_page.find(self.base_page.locators.INVALID_DATA_DIV).is_displayed()
        assert f'{self.url}/login' == self.driver.current_url
