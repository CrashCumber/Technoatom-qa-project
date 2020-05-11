import time
import pytest
import selenium
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base_ui import BaseCase
from ui.fixtures import *


class TestUI(BaseCase):

    @pytest.mark.skip(reason='TEMP')
    @pytest.mark.UI
    def test_log_info(self, auto):
        self.base_page = auto
        vk_id = self.base_page.find(self.main_page.locators.LOG_VK_ID, timeout=10).text
        name = self.base_page.find(self.main_page.locators.LOG_USERNAME, timeout=10).text

        vk_id = int(vk_id.split()[-1])
        assert vk_id == 1

        name = name.split()[-1]
        assert name == self.base_page.user

    @pytest.mark.UI
    @pytest.mark.skip(reason='TEMP')
    def test_python_fact(self, auto):
        self.base_page = auto
        fact = self.base_page.find(self.main_page.locators.FACT_PYTHON_DIV, timeout=10).text
        assert fact

    @pytest.mark.skip(reason='TEMP')
    def test_python_history(self, auto):
        self.base_page = auto
        events = self.base_page.find(self.main_page.locators.PYTHON_BUTTON, timeout=10)

        ac = ActionChains(self.driver)
        ac.move_to_element(events).perform()

        self.base_page.find(self.main_page.locators.PYTHON_HISTORY_BUTTON).click()

        assert 'history' in self.driver.page_source
        assert 'python' in self.driver.page_source

    @pytest.mark.skip(reason='TEMP')
    def test_flask(self, auto):
        self.base_page = auto
        events = self.base_page.find(self.main_page.locators.PYTHON_BUTTON, timeout=10)

        ac = ActionChains(self.driver)
        ac.move_to_element(events).perform()

        self.base_page.find(self.main_page.locators.FLASK_BUTTON).click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        assert 'flask' in self.driver.page_source
        self.driver.close()
        self.driver.switch_to.window(windows[0])

    @pytest.mark.skip(reason='TEMP')
    def test_linux_centos(self, auto):
        self.base_page = auto
        events = self.base_page.find(self.main_page.locators.LINUX_BUTTON, timeout=10)

        ac = ActionChains(self.driver)
        ac.move_to_element(events).perform()

        self.base_page.find(self.main_page.locators.CENTOS_BUTTON).click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        assert 'centos' in self.driver.page_source
        self.driver.close()
        self.driver.switch_to.window(windows[0])

    @pytest.mark.skip(reason='TEMP')
    def test_wireshark_news(self, auto):
        self.base_page = auto
        events = self.base_page.find(self.main_page.locators.NETWORK_BUTTON, timeout=10)

        ac = ActionChains(self.driver)
        ac.move_to_element(events).perform()

        self.base_page.find(self.main_page.locators.NEWS_BUTTON).click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        assert 'News' in self.driver.page_source
        assert 'Wireshark' in self.driver.page_source

        self.driver.close()
        self.driver.switch_to.window(windows[0])

    @pytest.mark.skip(reason='TEMP')
    def test_wireshark_download(self, auto):
        self.base_page = auto
        events = self.base_page.find(self.main_page.locators.NETWORK_BUTTON, timeout=10)

        ac = ActionChains(self.driver)
        ac.move_to_element(events).perform()

        self.base_page.find(self.main_page.locators.DOWNLOAD_BUTTON).click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        assert 'Download' in self.driver.page_source
        assert 'Wireshark' in self.driver.page_source

        self.driver.close()
        self.driver.switch_to.window(windows[0])

    @pytest.mark.skip(reason='TEMP')
    def test_tcp_example(self, auto):
        self.base_page = auto
        events = self.base_page.find(self.main_page.locators.NETWORK_BUTTON, timeout=10)

        ac = ActionChains(self.driver)
        ac.move_to_element(events).perform()

        self.base_page.find(self.main_page.locators.TCPEXAMP_BUTTON).click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        assert 'Tcpdump Examples' in self.driver.page_source

        self.driver.close()
        self.driver.switch_to.window(windows[0])

    @pytest.mark.UI
    @pytest.mark.skip(reason='TEMP')
    def test_future(self, auto):
        self.base_page = auto
        self.base_page.find(self.main_page.locators.FUT_INTERNET_BUTTON, timeout=10).click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        assert 'https://www.popularmechanics.com/technology/infrastructure/a29666802/future-of-the-internet/' == self.driver.current_url
        self.driver.close()
        self.driver.switch_to.window(windows[0])

    @pytest.mark.UI
    @pytest.mark.skip(reason='TEMP')
    def test_api(self, auto):
        self.base_page = auto
        self.base_page.find(self.main_page.locators.API_BUTTON, timeout=10).click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        assert 'Api' == self.driver.page_source
        self.driver.close()
        self.driver.switch_to.window(windows[0])

    @pytest.mark.UI
    @pytest.mark.skip(reason='TEMP')
    def test_smtp(self, auto):
        self.base_page = auto
        self.base_page.find(self.main_page.locators.SMTP_BUTTON, timeout=10).click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        assert 'SMTP' == self.driver.page_source
        self.driver.close()
        self.driver.switch_to.window(windows[0])

    @pytest.mark.UI
    @pytest.mark.skip(reason='TEMP')
    def test_python(self, auto):
        self.base_page = auto
        self.base_page.find(self.main_page.locators.PYTHON_BUTTON, timeout=10).click()
        assert 'https://www.python.org/' == self.driver.current_url

    @pytest.mark.skip(reason='TEMP')
    @pytest.mark.UI
    def test_good_authorization(self):
        user = 'valentina'
        password = 'valentina'
        self.base_page.authorization(user, password)
        assert 'http://0.0.0.0:8080/welcome/' == self.driver.current_url

    @pytest.mark.UI
    @pytest.mark.skip(reason='TEMP')
    def test_bad_authorization(self):
        user = 'qwertyuiopqwe'   #qwertyuiop5567676
        password = 'qwertyuiopqwertyuiop'
        self.base_page.authorization(user, password)

        assert self.base_page.find(self.base_page.locators.INVALID_LENGTH_DIV).is_displayed()
        assert 'http://0.0.0.0:8080/login' == self.driver.current_url

    @pytest.mark.skip(reason='TEMP')
    @pytest.mark.UI
    def test_create_account(self):
        date = ['igorivanov', 'igor@mail.ru', 'igorivanov']
        self.base_page.get_create_account_page()
        self.reg_page.create_account(date[0], date[2],  date[1])
        time.sleep(6)
        assert 'http://0.0.0.0:8080/welcome/' == self.driver.current_url

    @pytest.mark.skip(reason='TEMP')
    @pytest.mark.UI
    def test_invalid_data_account(self):
        date = ['igorivanovohrogorhgo', 'igormail.ru', 'igorivanov']
        self.base_page.get_create_account_page()
        self.reg_page.create_account(date[0], date[2], date[1])
        assert self.base_page.find(self.reg_page.locators.INVALID_NAME_DIV).is_displayed()
        assert self.base_page.find(self.reg_page.locators.INVALID_EMAIL_DIV).is_displayed()
        assert 'http://0.0.0.0:8080/reg/' == self.driver.current_url



