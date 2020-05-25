from tests.base_ui import BaseCase
from ui.fixtures import *


@pytest.mark.UI
class TestUIBasePage(BaseCase):

    @allure.title('Авторизация пользователя')
    @pytest.mark.UI_AUTO
    def test_existent_user_authorization(self):
        """ Авторизация валидного существующего пользователя.
        Ввод данных в поля авторизации.
        Перевод на главную страницу приложения.
        """

        user = self.base_page.user
        password = self.base_page.password
        self.base_page.authorization(user, password)
        assert f'{self.url}/welcome/' == self.driver.current_url

    @allure.title('Авторизация пользователя с невалидным именем')
    @pytest.mark.UI_AUTO
    def test_invalid_length_username_authorization(self):
        """ Авторизация невалидного существующего пользователя.
        Ввод данных в поля авторизации.
        Появление окна с предупреждением о невалидном имене, пользователь остается на странице авторизации.
        """

        user = 'invalid_very_big_username'
        password = 'valid_pass'
        self.base_page.authorization(user, password)

        assert self.base_page.find(self.base_page.locators.INVALID_USERNAME_LENGTH_DIV).is_displayed()
        assert f'{self.url}/login' == self.driver.current_url

    @allure.title('Авторизация несуществующего пользователя')
    @pytest.mark.UI_AUTO
    def test_nonexistent_user_authorization(self):
        """ Авторизация несуществующего пользователя.
        Ввод данных в поля авторизации.
        Появление окна с предупреждением о невалидной данных, пользователь остается на странице авторизации.
        """

        user = 'nonexistent'
        password = 'nonexistent_pass'
        self.base_page.authorization(user, password)

        assert self.base_page.find(self.base_page.locators.INVALID_DATA_DIV).is_displayed()
        assert f'{self.url}/login' == self.driver.current_url
