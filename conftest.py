import threading
import time

import docker

from api.fixtures import *
import pytest
from ui.fixtures import *
from dataclasses import dataclass
from api.api_client import ApiClient
import requests



# @pytest.fixture(scope='session')
# def docker_api():
#     docker_client = docker.from_env()
#
#     db = docker_client.containers.get('project_qa_db_1')
#     db.start()
#
#     mock = docker_client.containers.get('project_qa_vk_api_mock_1')
#     mock.start()
#
#     app = docker_client.containers.get('project_qa_myapp_1')
#     app.start()
#     time.sleep(6)
#
#     yield docker_client
#
#     app.stop()
#     mock.stop()
#     db.stop()


def pytest_addoption(parser):
    parser.addoption('--url', default='http://0.0.0.0:8082')  # for selenoid http://myapp:8082
    parser.addoption('--browser', default='chrome')
    parser.addoption('--browser_ver', default='latest')
    parser.addoption('--selenoid', default=None)


@pytest.fixture(scope='session')
def config(request, docker_api):
    url = request.config.getoption('--url')
    browser = request.config.getoption('--browser')
    version = request.config.getoption('--browser_ver')
    selenoid = request.config.getoption('--selenoid')       #true or none
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
    client = ApiClient(config_api.URL, user, password, email)
    # client.start()
    yield client
    # client.delete_users()


