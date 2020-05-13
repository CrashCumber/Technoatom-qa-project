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
def driver(config_ui):
    browser = config_ui['browser']
    version = config_ui['version']
    url = config_ui['url']
    selenoid = False
    if not selenoid:
        manager = ChromeDriverManager(version=version)
        driver = webdriver.Chrome(executable_path=manager.install())
    else:
        options = ChromeOptions()
        capabilities = {'acceptInsecureCerts': True,
                        'browserName': 'chrome',
                        'version': '80.0'}
        driver = webdriver.Remote(command_executor=selenoid,
                                  options=options,
                                  desired_capabilities=capabilities)
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.close()
