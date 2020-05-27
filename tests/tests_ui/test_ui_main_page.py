import time
from selenium.webdriver import ActionChains
from tests.base_ui import BaseCase
from ui.fixtures import *


class NewPageException(Exception):
    print('Страница отображается не в новой вкладке')


@pytest.mark.UI
class TestUIMaimPage(BaseCase):

    @allure.title("Масштабируемость окна приложения")
    @pytest.mark.UI_MAIN
    def test_window_size(self, auto):
        """ Корректность меню при уменьшении страницы.
        Уменьшение окна и поиск кнопки home.
        Кнопка Home видима и доступна.
        """

        self.base_page = auto

        self.driver.set_window_size(350, 750)
        time.sleep(4)

        assert self.base_page.find(self.main_page.locators.HOME_BUTTON).is_displayed(), 'Верхнее меню исчезло из поля видимости'
        self.driver.maximize_window()

    @allure.title("Наличие идентификатора пользователя(имя и vk_id)")
    @pytest.mark.UI_MAIN
    def test_log_info(self, auto):
        """ Наличие и корректность информации о текущем пользователе в правом верхем углу.
        Поиск объекта с данными.
        Имя и vk_id успешно отображены.
        """

        self.base_page = auto
        vk_id = self.base_page.find(self.main_page.locators.LOG_VK_ID, timeout=3).text
        name = self.base_page.find(self.main_page.locators.LOG_USERNAME, timeout=3).text

        vk_id = int(vk_id.split()[-1])
        assert vk_id == 1

        name = name.split()[-1]
        assert name == self.base_page.user

    @allure.title("Наличие факта о языке программирования python")
    @pytest.mark.UI_MAIN
    def test_python_fact(self, auto):
        """ Отображение в нижней части страницы случайного мотивационного факта о python.
        Поиск объекта с данными.
        Факт присутствует.
        """
        self.base_page = auto
        fact = self.base_page.find(self.main_page.locators.FACT_PYTHON_DIV, timeout=3).text
        assert fact

    @allure.title("Корректность ссылки на страницу с исторей питона в новой вкладке браузера")
    @pytest.mark.UI_MAIN
    def test_python_history_link(self, auto):
        """Корректность ссылки на страницу с исторей питона.
        Нажатие на кпопку "Python history" в выдвигающемся меню.
        Новая вкладка с корректной страницей.
        """
        try:
            self.base_page = auto
            events = self.base_page.find(self.main_page.locators.PYTHON_BUTTON, timeout=3)

            ac = ActionChains(self.driver)
            ac.move_to_element(events).perform()

            self.base_page.find(self.main_page.locators.PYTHON_HISTORY_BUTTON).click()

            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[1])
            title = self.driver.title

            assert ('History' or 'history') in title, title
            assert ('Python' or 'python') in title, title

            self.driver.close()
            self.driver.switch_to.window(windows[0])
        except IndexError:
            raise NewPageException('Страница отображается не в новой вкладке')

    @allure.title("Корректность ссылки на страницу с информацией о flask в новой вкладке браузера")
    @pytest.mark.UI_MAIN
    def test_flask_link(self, auto):
        """Корректность ссылки на страницу с информацией о flask.
        Нажатие на кпопку "About flask" в выдвигающемся меню.
        Новая вкладка с корректной страницей.
        """
        try:
            self.base_page = auto
            events = self.base_page.find(self.main_page.locators.PYTHON_BUTTON, timeout=3)

            ac = ActionChains(self.driver)
            ac.move_to_element(events).perform()

            self.base_page.find(self.main_page.locators.FLASK_BUTTON).click()

            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[1])
            title = self.driver.title

            assert ('Flask' or 'flask') in title, title

            self.driver.close()
            self.driver.switch_to.window(windows[0])
        except IndexError:
            raise NewPageException('Страница отображается не в новой вкладке')

    @allure.title("Корректность ссылки на страницу с информацией о centos в новой вкладке браузера")
    @pytest.mark.UI_MAIN
    def test_linux_centos_link(self, auto):
        """Корректность ссылки на страницу с информацией о centos.
        Нажатие на кпопку "Download centos7" в выдвигающемся меню.
        Новая вкладка с корректной страницей.
        """
        try:
            self.base_page = auto
            events = self.base_page.find(self.main_page.locators.LINUX_BUTTON, timeout=3)

            ac = ActionChains(self.driver)
            ac.move_to_element(events).perform()

            self.base_page.find(self.main_page.locators.CENTOS_BUTTON).click()

            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[1])
            title = self.driver.title

            assert ('centos' or 'Centos') in title, 'Ссылка ведет не на стрицу centos'

            self.driver.close()
            self.driver.switch_to.window(windows[0])

        except IndexError:
            raise NewPageException('Страница отображается не в новой вкладке')

    @allure.title("Корректность ссылки на страницу с новостями о wireshark в новой вкладке браузера")
    @pytest.mark.UI_MAIN
    def test_wireshark_news_link(self, auto):
        """Корректность ссылки на страницу с новостями о wireshark.
        Нажатие на кпопку "wireshark news" в выдвигающемся меню.
        Новая вкладка с корректной страницей.
        """
        try:
            self.base_page = auto
            events = self.base_page.find(self.main_page.locators.NETWORK_BUTTON, timeout=3)

            ac = ActionChains(self.driver)
            ac.move_to_element(events).perform()

            self.base_page.find(self.main_page.locators.NEWS_BUTTON).click()

            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[1])
            title = self.driver.title

            assert ('News' or 'news') in title, title
            assert ('Wireshark' or 'wireshark') in title, title

            self.driver.close()
            self.driver.switch_to.window(windows[0])
        except IndexError:
            raise NewPageException('Страница отображается не в новой вкладке')

    @allure.title("Корректность ссылки на страницу с установщиком wireshark в новой вкладке браузера")
    @pytest.mark.UI_MAIN
    def test_wireshark_download_link(self, auto):
        """Корректность ссылки на страницу с установщиком wireshark.
        Нажатие на кпопку "wireshark download" в выдвигающемся меню.
        Новая вкладка с корректной страницей.
        """

        try:
            self.base_page = auto
            events = self.base_page.find(self.main_page.locators.NETWORK_BUTTON, timeout=3)

            ac = ActionChains(self.driver)
            ac.move_to_element(events).perform()

            self.base_page.find(self.main_page.locators.DOWNLOAD_BUTTON).click()

            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[1])
            url = self.driver.current_url

            assert 'download' in url
            assert 'wireshark' in url

            self.driver.close()
            self.driver.switch_to.window(windows[0])

        except IndexError:
            raise NewPageException('Страница отображается не в новой вкладке')

    @allure.title("Корректность ссылки на страницу с примерами TCP в новой вкладке браузера")
    @pytest.mark.UI_MAIN
    def test_tcp_example(self, auto):
        """Корректность ссылки на страницу с примерами TCP.
        Нажатие на кпопку "TCPDump Examples" в выдвигающемся меню.
        Новая вкладка с корректной страницей.
        """
        try:
            self.base_page = auto
            events = self.base_page.find(self.main_page.locators.NETWORK_BUTTON, timeout=3)

            ac = ActionChains(self.driver)
            ac.move_to_element(events).perform()

            self.base_page.find(self.main_page.locators.TCPEXAMP_BUTTON).click()

            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[1])
            title = self.driver.title

            assert ('Tcpdump' or 'tcpdump') in title, title
            assert ('Examples' or 'examples') in title, title

            self.driver.close()
            self.driver.switch_to.window(windows[0])
        except IndexError:
            raise NewPageException('Страница отображается не в новой вкладке')

    @allure.title("Корректность ссылки на страницу с будущем интернета в новой вкладке браузера")
    @pytest.mark.UI_MAIN
    def test_future_link(self, auto):
        """Корректность ссылки на страницу с информацией о centos.
        Нажатие на иконку под надписью "Future of Internet".
        Новая вкладка с корректной страницей.
        """
        try:
            self.base_page = auto
            self.base_page.find(self.main_page.locators.FUT_INTERNET_BUTTON, timeout=3).click()

            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[1])
            url = self.driver.current_url

            assert 'future' in url, url
            assert 'internet' in url, url

            self.driver.close()
            self.driver.switch_to.window(windows[0])

        except IndexError:
            raise NewPageException('Страница отображается не в новой вкладке')

    @allure.title("Корректность ссылки на страницу с API в новой вкладке браузера")
    @pytest.mark.UI_MAIN
    def test_api_link(self, auto):
        """Корректность ссылки на страницу с API.
        Нажатие на иконку под надписью "What is an API?".
        Новая вкладка с корректной страницей.
        """
        try:
            self.base_page = auto
            self.base_page.find(self.main_page.locators.API_BUTTON, timeout=3).click()

            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[1])
            title = self.driver.title

            assert ('Application programming interface' or 'API') in title, title

            self.driver.close()
            self.driver.switch_to.window(windows[0])
        except IndexError:
            raise NewPageException

    @allure.title("Корректность ссылки на страницу с SMTP в новой вкладке браузера")
    @pytest.mark.UI_MAIN
    def test_smtp_link(self, auto):
        """Корректность ссылки на страницу с SMTP.
        Нажатие на иконку под надписью "Lets talk about SMTP?".
        Новая вкладка с корректной страницей.
        """
        try:
            self.base_page = auto
            self.base_page.find(self.main_page.locators.SMTP_BUTTON, timeout=3).click()

            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[1])
            title = self.driver.title

            assert 'SMTP' in title

            self.driver.close()
            self.driver.switch_to.window(windows[0])

        except IndexError:
            raise NewPageException('Страница отображается не в новой вкладке')

    @allure.title("Корректность ссылки на страницу питона в новой вкладке браузера")
    @pytest.mark.UI_MAIN
    def test_python_link(self, auto):
        """Корректность ссылки на страницу питона.
        Нажатие на кпопку "Python".
        Новая вкладка с корректной страницей.
        """

        try:
            self.base_page = auto
            self.base_page.find(self.main_page.locators.PYTHON_BUTTON, timeout=3).click()
            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[1])
            title = self.driver.title

            assert 'python' in title, title

            self.driver.close()
            self.driver.switch_to.window(windows[0])
        except IndexError:
            raise NewPageException('Страница отображается не в новой вкладке')



