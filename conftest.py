import pytest
from ui.fixtures import *
from dataclasses import dataclass
from api.api_client import ApiClient
import requests


def pytest_addoption(parser):
    parser.addoption('--url', default='http://0.0.0.0:8082/')  # for selenoid http://myapp:8082
    parser.addoption('--browser', default='chrome')
    parser.addoption('--browser_ver', default='latest')
    parser.addoption('--selenoid', default=None)


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    browser = request.config.getoption('--browser')
    version = request.config.getoption('--browser_ver')
    selenoid = request.config.getoption('--selenoid') #true or none
    yield {'browser': browser, 'version': version, 'url': url, 'selenoid': selenoid}
    requests.get('http://0.0.0.0:5000/delete_users/')


@dataclass
class Settings:
    URL: str = None


@pytest.fixture(scope='session')
def config_api() -> Settings:
    settings = Settings(URL="http://0.0.0.0:8082/")
    yield settings
    requests.get('http://0.0.0.0:5000/delete_users/')


@pytest.fixture(scope='function')
def api_client(config_api):
    user = 'valentina'
    password = 'valentina'
    email = ''
    return ApiClient(config_api.URL, user, password, email)

