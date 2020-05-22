import time
from selenium.webdriver import ActionChains
from tests.base_ui import BaseCase
from ui.fixtures import *



class TestUIMaimPage(BaseCase):

    @pytest.mark.UI_MAIN
    def test_window_size(self, auto):
        self.base_page = auto

        self.driver.set_window_size(350, 750)
        time.sleep(4)
        assert self.base_page.find(self.main_page.locators.HOME_BUTTON).is_displayed()
        self.driver.maximize_window()

    @pytest.mark.UI_MAIN
    def test_log_info(self, auto):
        self.base_page = auto
        vk_id = self.base_page.find(self.main_page.locators.LOG_VK_ID, timeout=3).text
        name = self.base_page.find(self.main_page.locators.LOG_USERNAME, timeout=3).text

        vk_id = int(vk_id.split()[-1])
        assert vk_id == 1

        name = name.split()[-1]
        assert name == self.base_page.user

    @pytest.mark.UI_MAIN
    def test_python_fact(self, auto):
        self.base_page = auto
        fact = self.base_page.find(self.main_page.locators.FACT_PYTHON_DIV, timeout=3).text
        assert fact

    @pytest.mark.UI_MAIN
    def test_python_history_link(self, auto):
        self.base_page = auto
        events = self.base_page.find(self.main_page.locators.PYTHON_BUTTON, timeout=3)

        ac = ActionChains(self.driver)
        ac.move_to_element(events).perform()

        self.base_page.find(self.main_page.locators.PYTHON_HISTORY_BUTTON).click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

        assert 'History' in self.driver.title
        assert 'Python' in self.driver.title

        self.driver.close()
        self.driver.switch_to.window(windows[0])

    @pytest.mark.UI_MAIN
    def test_flask_link(self, auto):
        self.base_page = auto
        events = self.base_page.find(self.main_page.locators.PYTHON_BUTTON, timeout=3)

        ac = ActionChains(self.driver)
        ac.move_to_element(events).perform()

        self.base_page.find(self.main_page.locators.FLASK_BUTTON).click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

        assert ('flask' in self.driver.title or 'Flask' in self.driver.title)

        self.driver.close()
        self.driver.switch_to.window(windows[0])

    @pytest.mark.UI_MAIN
    def test_linux_centos_link(self, auto):
        self.base_page = auto
        events = self.base_page.find(self.main_page.locators.LINUX_BUTTON, timeout=3)

        ac = ActionChains(self.driver)
        ac.move_to_element(events).perform()

        self.base_page.find(self.main_page.locators.CENTOS_BUTTON).click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

        assert ('centos' in self.driver.title or 'Centos' in self.driver.title)

        self.driver.close()
        self.driver.switch_to.window(windows[0])

    @pytest.mark.UI_MAIN
    def test_wireshark_news_link(self, auto):
        self.base_page = auto
        events = self.base_page.find(self.main_page.locators.NETWORK_BUTTON, timeout=3)

        ac = ActionChains(self.driver)
        ac.move_to_element(events).perform()

        self.base_page.find(self.main_page.locators.NEWS_BUTTON).click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

        assert ('News' in self.driver.title or 'news' in self.driver.title)
        assert ('Wireshark' in self.driver.title or 'wireshark' in self.driver.title)

        self.driver.close()
        self.driver.switch_to.window(windows[0])

    @pytest.mark.UI_MAIN
    def test_wireshark_download_link(self, auto):
        self.base_page = auto
        events = self.base_page.find(self.main_page.locators.NETWORK_BUTTON, timeout=3)

        ac = ActionChains(self.driver)
        ac.move_to_element(events).perform()

        self.base_page.find(self.main_page.locators.DOWNLOAD_BUTTON).click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

        assert 'Download' in self.driver.title or 'download' in self.driver.current_url
        assert 'Wireshark' in self.driver.title or 'wireshark' in self.driver.current_url

        self.driver.close()
        self.driver.switch_to.window(windows[0])

    @pytest.mark.UI_MAIN
    def test_tcp_example(self, auto):
        self.base_page = auto
        events = self.base_page.find(self.main_page.locators.NETWORK_BUTTON, timeout=3)

        ac = ActionChains(self.driver)
        ac.move_to_element(events).perform()

        self.base_page.find(self.main_page.locators.TCPEXAMP_BUTTON).click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

        assert 'Tcpdump' in self.driver.title or 'tcpdump' in self.driver.title
        assert 'Examples' in self.driver.title or 'tcpdump' in self.driver.title

        self.driver.close()
        self.driver.switch_to.window(windows[0])

    @pytest.mark.UI_MAIN
    def test_future_link(self, auto):
        self.base_page = auto
        self.base_page.find(self.main_page.locators.FUT_INTERNET_BUTTON, timeout=3).click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

        assert 'future' in self.driver.current_url
        assert 'internet' in self.driver.current_url

        self.driver.close()
        self.driver.switch_to.window(windows[0])

    @pytest.mark.UI_MAIN
    def test_api_link(self, auto):
        self.base_page = auto
        self.base_page.find(self.main_page.locators.API_BUTTON, timeout=3).click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

        assert ('Application programming interface' in self.driver.page_source or 'API' in self.driver.page_source)

        self.driver.close()
        self.driver.switch_to.window(windows[0])

    @pytest.mark.UI_MAIN
    def test_smtp_link(self, auto):
        self.base_page = auto
        self.base_page.find(self.main_page.locators.SMTP_BUTTON, timeout=3).click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

        assert 'SMTP' in self.driver.title

        self.driver.close()
        self.driver.switch_to.window(windows[0])

    @pytest.mark.UI_MAIN
    def test_python_link(self, auto):
        self.base_page = auto
        self.base_page.find(self.main_page.locators.PYTHON_BUTTON, timeout=3).click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

        assert 'python' in self.driver.title

        self.driver.close()
        self.driver.switch_to.window(windows[0])










#
# class LinkDataWithActionChain:
#
#     python_history = ('PYTHON_BUTTON', 'PYTHON_HISTORY_BUTTON', ['python', 'history'])
#     flask = ('PYTHON_BUTTON', 'FLASK_BUTTON', ['flask'])
#
#     linux_centos = ('LINUX_BUTTON', 'CENTOS_BUTTON', ['centos'])
#
#     wireshark_news = ('NETWORK_BUTTON', 'NEWS_BUTTON', ['wireshark', 'news'])
#     wireshark_download = ('NETWORK_BUTTON', 'DOWNLOAD_BUTTON', ['wireshark', 'downloads'])
#     tcp_example = ('NETWORK_BUTTON', 'TCPEXAMP_BUTTON', ['tcp'])
#
#
# class LinkData:
#     future = ('FUT_INTERNET_BUTTON', [])
#     api = ('API_BUTTON', ['API'])
#     smtp = ('SMTP_BUTTON', ['SMTP'])
#     python = ('PYTHON_BUTTON', ['python'])
