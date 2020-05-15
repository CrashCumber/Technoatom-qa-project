import time
from .base_page import BasePage
from ui.locators.locators import RegPageLocators


class RegPage(BasePage):
    locators = RegPageLocators()

    def create_account(self, user, password, email, password_repeated=None):

        user_field = self.find(self.locators.INPUT_NEW_NAME)
        user_field.clear()

        password_field = self.find(self.locators.INPUT_NEW_PASSWORD)
        password_field.clear()

        email_field = self.find(self.locators.INPUT_EMAIL)
        email_field.clear()

        password_repeat_field = self.find(self.locators.INPUT_REPEAT_PASSWORD)
        password_repeat_field.clear()

        if password_repeated:
            password_field.send_keys(password_repeated)
        else:
            password_field.send_keys(password)
        user_field.send_keys(user)
        email_field.send_keys(email)
        password_repeat_field.send_keys(password)
        time.sleep(1)

        self.find(self.locators.CHECK_BOX).click()
        time.sleep(1)

        self.find(self.locators.REGISTER_BUTTON).click()
