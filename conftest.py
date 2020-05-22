import datetime
import json
import os
import threading
import time
import docker
from api.fixtures import *
import pytest
from ui.fixtures import *
from dataclasses import dataclass
from api.api_client import ApiClient
import requests
import allure_pytest


@pytest.fixture(scope='session')
def docker_api():
    docker_client = docker.from_env()

    db = docker_client.containers.get('project_qa_db_1')
    db.start()

    mock = docker_client.containers.get('project_qa_vk_api_mock_1')
    mock.start()

    app = docker_client.containers.get('project_qa_myapp_1')
    app.start()
    start = datetime.datetime.now()
    time.sleep(3)

    yield docker_client

    app.stop()
    mock.stop()
    db.stop()
    data = []
    delta = (datetime.datetime.now() - start).seconds
    start=start.hour-3
    for i in app.logs(stream=True, since=start):
        print(i, type(i))
        # data.append(i.decode())
    #
    # DATA = json.dumps(data)
    # allure.attach(name='logs', body=DATA, attachment_type=allure.attachment_type.JSON )


def pytest_addoption(parser):
    parser.addoption('--url', default='http://0.0.0.0:8082')
    parser.addoption('--browser', default='chrome')
    parser.addoption('--browser_ver', default='latest')
    parser.addoption('--selenoid', default=None)


@pytest.fixture(scope='session')
def config(request, docker_api):
    url = request.config.getoption('--url')
    browser = request.config.getoption('--browser')
    version = request.config.getoption('--browser_ver')
    selenoid = request.config.getoption('--selenoid')       #true or none
    if selenoid:
        url = 'http://myapp:8082'
    return {'browser': browser, 'version': version, 'url': url, 'selenoid': selenoid}


@dataclass
class Settings:
    URL: str = None


@pytest.fixture(scope='session')
def config_api(docker_api) -> Settings:
    settings = Settings(URL="http://0.0.0.0:8082/")
    return settings


@pytest.fixture(scope='function')
def api_client(config_api):
    user = 'valentina'
    password = 'valentina'
    email = ''
    client = ApiClient(config_api.URL, user, password, email)
    # client.start()
    return client


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'driver' in item.fixturenames:
                    web_driver = item.funcargs['driver']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))
