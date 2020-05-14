import json
import requests
from faker import Faker
fake = Faker()


class URLS:
    ADD_USER = 'http://0.0.0.0:8080/api/add_user'

    DELETE_USER = 'http://0.0.0.0:8080/api/del_user/'
    BLOCK_USER = 'http://0.0.0.0:8080/api/block_user/'
    UNBLOCK_USER = 'http://0.0.0.0:8080/api/accept_user/'

    STATUS_APP = 'http://0.0.0.0:8080/status'
    AUTORIZATION = 'http://0.0.0.0:8080/login'
    USER_PAGE = 'http://0.0.0.0:8080/welcome/'
    LOGOUT = 'http://0.0.0.0:8080/logout'


class ApiClient:

    def __init__(self, url, user, password, email):
        self.base_url = url
        self.user = user
        self.password = password
        self.email = email
        self.session = requests.Session()
        # self.authorization(self.user, self.password)

    def _request(self, method, location, headers=None, data=None, redirect=False):
        response = self.session.request(method, location, headers=headers, data=data, allow_redirects=redirect)
        return response

    def form_valid_user_data(self, have_access=False, access_value=1):
        username = fake.last_name()
        while len(username) in range(10, 15):
            username = fake.last_name()

        password = fake.password()
        email = fake.email()
        if have_access:
            return {"username": username, "password": password, "email": email, "access": access_value}
        return {"username": username, "password": password, "email": email}

    def authorization(self, user, password):
        location = 'http://0.0.0.0:8080/login'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {
            'username': user,
            'password': password,
            'submit': 'Login'
        }
        response = self._request('POST', location, headers=headers, data=data)

        while response.status_code == 302:
            location = response.headers['Location']
            response = self._request('GET', location)

        return response

    def create(self, username, password, email):
        data = {
               "username": username,
               "password": password,
               "email": email
                }
        data = json.dumps(data)
        location = URLS.ADD_USER
        headers = {'Content-Type': 'application/json'}
        response = self._request('POST', location, headers=headers, data=data)
        return response

    def delete(self, user):
        location = URLS.DELETE_USER+user
        response = self._request('GET', location)
        return response

    def block(self, user):
        location = URLS.BLOCK_USER+user
        response = self._request('GET', location)
        return response

    def unblock(self, user):
        location = URLS.UNBLOCK_USER+user
        response = self._request('GET', location)
        return response

    def status(self):
        location = URLS.STATUS_APP
        response = self._request('GET', location)
        return response

    def get_user_from_db(self, username):
        location = f'http://0.0.0.0:5000/get_user/{username}'
        response = self._request('GET', location)
        return response

    def insert_user_in_db(self, data):
        location = f'http://0.0.0.0:5000/insert_user/'
        self._request('POST', location, data=data)

    def delete_user_from_db(self, username):
        location = f'http://0.0.0.0:5000/delete_user/{username}'
        response = self._request('GET', location)
        return response

    def logout(self):
        location = URLS.LOGOUT
        response = self._request('GET', location)
        while response.status_code == 302:
            location = response.headers['Location']
            response = self._request('GET', location)
        return response
