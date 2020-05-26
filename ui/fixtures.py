import allure
import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from ui.pages.base_page import BasePage
from ui.pages.reg_page import RegPage
from ui.pages.main_page import MainPage


@pytest.fixture(scope='function')
def base_page(driver):
    return BasePage(driver)


@pytest.fixture(scope='function')
def reg_page(driver):
    return RegPage(driver)


@pytest.fixture(scope='function')
def main_page(driver):
    return MainPage(driver)


@pytest.fixture(scope="function")
def auto(driver):
    page = BasePage(driver)
    page.authorization(page.user, page.password)
    return BasePage(page.driver)


@pytest.fixture(scope='function')
def driver(config):
    browser = config['browser']
    version = config['version']
    url = config['url']
    selenoid = config['selenoid']
    if not selenoid:
        manager = ChromeDriverManager(version=version)
        driver = webdriver.Chrome(executable_path=manager.install())
    else:
        options = ChromeOptions()
        capabilities = {'acceptInsecureCerts': True,
                        'browserName': 'chrome',
                        'version': '83.0'}
        driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                                  options=options,
                                  desired_capabilities=capabilities)
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()









from selenium.webdriver import ActionChains


# @pytest.fixture(scope='function')
# def menu_python_links(setup, auto):
#     setup.base_page = auto
#     events = driver.base_page.find(setup.main_page.locators.PYTHON_BUTTON, timeout=3)
#
#     ac = ActionChains(setup.driver)
#     ac.move_to_element(events).perform()
#         windows = self.driver.window_handles
#         self.driver.switch_to.window(windows[1])
#     yield
#     setup.driver.close()
#     setup.driver.switch_to.window(windows[0])

#
# @pytest.fixture(scope='function')
# def menu_linux_links(driver):
#     return BasePage(driver)
#
# @pytest.fixture(scope='function')
# def menu__links(driver):
#     return BasePage(driver)
