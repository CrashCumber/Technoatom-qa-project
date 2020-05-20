from tests.base_api import BaseCase
import pytest


class TestAPIBlockage(BaseCase):

    @pytest.mark.API_BLOCK #+++
    def test_block_user_status_code(self, api_client, user_with_access):
        data = user_with_access
        response = api_client.block(data["username"])
        assert response.status_code == 200

    @pytest.mark.API_BLOCK # +++
    def test_block_user_data_in_db(self, api_client, user_with_access):
        data = user_with_access

        response = api_client.block(data["username"])
        assert response.status_code == 200

        response_data = api_client.get_user_from_db(data["username"])
        assert response_data["access"] == 0

    @pytest.mark.API_BLOCK#+++
    def test_unblock_user_status_code(self, api_client, user_with_zero_access):
        data = user_with_zero_access
        response = api_client.unblock(data["username"])
        assert response.status_code == 200, "Response status code isn't 200"

    @pytest.mark.API_BLOCK # +++
    def test_unblock_user_data_in_db(self, api_client, user_with_zero_access):
        data = user_with_zero_access
        api_client.unblock(data["username"])
        response_data = api_client.get_user_from_db(data["username"])
        assert response_data["access"] == 1, response_data

    @pytest.mark.API_BLOCK #+++
    def test_block_nonexistent_user(self, api_client):
        username = "nonexistent"

        response = api_client.block(username)
        assert response.status_code == 404

        response = api_client.unblock(username)
        assert response.status_code == 404

    @pytest.mark.API_BLOCK #+++
    def test_auto_block_user(self, api_client, user_with_zero_access):
        data = user_with_zero_access

        response = api_client.authorization(data["username"], data["password"])
        assert response.status_code == 401

    @pytest.mark.API_BLOCK
    def test_block_while_active(self, api_client, user_with_access):
        data = user_with_access
        api_client.active_user(data["username"])

        api_client.block(data["username"])

        response_data = api_client.get_user_from_db(data["username"])
        assert response_data["access"] == 0, response_data
        assert response_data["active"] == 0, response_data



