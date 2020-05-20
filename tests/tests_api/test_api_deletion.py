from tests.base_api import BaseCase
import pytest


class TestAPIDeletion(BaseCase):

    @pytest.mark.API_DELETION #+++
    def test_delete_user_status_code(self, api_client, user_data):
        data = user_data

        response = api_client.delete(data["username"])
        assert response.status_code == 204,  "Response status code isn't 204"

    @pytest.mark.API_DELETION #+++
    def test_delete_user_from_db(self, api_client, user_data):
        data = user_data
        api_client.delete(data["username"])

        response_data = api_client.get_user_from_db(data["username"])

        assert response_data == None

    @pytest.mark.API_DELETION #+++
    def test_delete_nonexistent_user_status_code(self, api_client):
        username = "nonexistent"

        response = api_client.delete(username)
        assert response.status_code == 404

    @pytest.mark.API_DELETION  # +++
    def test_delete_nonexistent_data_in_db(self, api_client):
        username = "nonexistent"

        api_client.delete(username)

        response_data = api_client.get_user_from_db(username)
        assert response_data == None
