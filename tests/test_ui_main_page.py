import time
import pytest
import selenium
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base_ui import BaseCase
from ui.fixtures import *

class TestUIMaimPage(BaseCase):

    @pytest.mark.UI
    def test_log_info(self, auto):
        self.base_page = auto

        self.driver.set_window_size(550, 750)
        time.sleep(4)
        assert self.base_page.find(self.main_page.locators.HOME_BUTTON).is_displayed()
        self.driver.maximize_window()


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
    def test_python_fact(self, auto):
        self.base_page = auto
        fact = self.base_page.find(self.main_page.locators.FACT_PYTHON_DIV, timeout=10).text
        assert fact

    @pytest.mark.UI
    def test_python_history_link(self, auto):
        self.base_page = auto
        events = self.base_page.find(self.main_page.locators.PYTHON_BUTTON, timeout=10)

        ac = ActionChains(self.driver)
        ac.move_to_element(events).perform()

        self.base_page.find(self.main_page.locators.PYTHON_HISTORY_BUTTON).click()

        assert 'history' in self.driver.page_source
        assert 'python' in self.driver.page_source

    @pytest.mark.UI
    def test_flask_link(self, auto):
        self.base_page = auto
        events = self.base_page.find(self.main_page.locators.PYTHON_BUTTON, timeout=10)

        ac = ActionChains(self.driver)
        ac.move_to_element(events).perform()

        self.base_page.find(self.main_page.locators.FLASK_BUTTON).click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

        assert ('flask' in self.driver.page_source or 'Flask' in self.driver.page_source)

        self.driver.close()
        self.driver.switch_to.window(windows[0])

    @pytest.mark.UI
    def test_linux_centos_link(self, auto):
        self.base_page = auto
        events = self.base_page.find(self.main_page.locators.LINUX_BUTTON, timeout=10)

        ac = ActionChains(self.driver)
        ac.move_to_element(events).perform()

        self.base_page.find(self.main_page.locators.CENTOS_BUTTON).click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

        assert ('centos' in self.driver.page_source or 'Centos' in self.driver.page_source)

        self.driver.close()
        self.driver.switch_to.window(windows[0])

    @pytest.mark.UI
    def test_wireshark_news_link(self, auto):
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

    @pytest.mark.UI
    def test_wireshark_download_link(self, auto):
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

    @pytest.mark.UI
    def test_tcp_example(self, auto):
        self.base_page = auto
        events = self.base_page.find(self.main_page.locators.NETWORK_BUTTON, timeout=10)

        ac = ActionChains(self.driver)
        ac.move_to_element(events).perform()

        self.base_page.find(self.main_page.locators.TCPEXAMP_BUTTON).click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

        assert 'Tcpdump' in self.driver.page_source
        assert 'Examples' in self.driver.page_source

        self.driver.close()
        self.driver.switch_to.window(windows[0])

    @pytest.mark.UI
    def test_future_link(self, auto):
        self.base_page = auto
        self.base_page.find(self.main_page.locators.FUT_INTERNET_BUTTON, timeout=10).click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

        assert 'future' in self.driver.page_source
        assert 'internet' in self.driver.page_source

        self.driver.close()
        self.driver.switch_to.window(windows[0])

    @pytest.mark.UI
    def test_api_link(self, auto):
        self.base_page = auto
        self.base_page.find(self.main_page.locators.API_BUTTON, timeout=10).click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

        assert ('Application programming interface' in self.driver.page_source or 'API' in self.driver.page_source)

        self.driver.close()
        self.driver.switch_to.window(windows[0])

    @pytest.mark.UI
    def test_smtp_link(self, auto):
        self.base_page = auto
        self.base_page.find(self.main_page.locators.SMTP_BUTTON, timeout=10).click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

        assert 'SMTP' in self.driver.page_source

        self.driver.close()
        self.driver.switch_to.window(windows[0])

    @pytest.mark.UI
    def test_python_link(self, auto):
        self.base_page = auto
        self.base_page.find(self.main_page.locators.PYTHON_BUTTON, timeout=10).click()
        assert 'https://www.python.org/' == self.driver.current_url
