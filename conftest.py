import pytest
from ui.fixtures import *
from dataclasses import dataclass
from api.api_client import ApiClient


def pytest_addoption(parser):
    parser.addoption('--url', default='http://0.0.0.0:8082/')
    parser.addoption('--browser', default='chrome')
    parser.addoption('--browser_ver', default='latest')
    parser.addoption('--selenoid', default=None)


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    browser = request.config.getoption('--browser')
    version = request.config.getoption('--browser_ver')
    selenoid = request.config.getoption('--selenoid')
    return {'browser': browser, 'version': version, 'url': url, 'selenoid': selenoid}


@dataclass
class Settings:
    URL: str = None


@pytest.fixture(scope='session')
def config_api() -> Settings:
    settings = Settings(URL="http://0.0.0.0:8082/")
    return settings


@pytest.fixture(scope='function')
def api_client(config_api):
    user = 'valentina'
    password = 'valentina'
    email = ''
    return ApiClient(config_api.URL, user, password, email)
