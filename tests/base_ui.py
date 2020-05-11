import pytest
from ui.fixtures import *
from ui.pages.base_page import BasePage
from ui.pages.reg_page import RegPage
from ui.pages.main_page import MainPage



class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request):
        self.driver = driver
        self.config = config
        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.reg_page: RegPage = request.getfixturevalue('reg_page')
        self.main_page: MainPage = request.getfixturevalue('main_page')

