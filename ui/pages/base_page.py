from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from ui.locators.locators import BaseLocators
from faker import Faker
fake = Faker()
RETRY_COUNT = 2


class BasePage:
    locators = BaseLocators()

    def __init__(self, driver):
        self.driver = driver
        self.user = 'valentina'
        self.password = 'valentina'

    def get_create_account_page(self):
        self.find(self.locators.CREATE_ACCOUNT_BUTTON).click()

    def find(self, locator, timeout=None):
        try:
            s = self.wait(timeout).until(EC.presence_of_all_elements_located(locator))
            if len(s) == 1:
                return self.wait(timeout).until(EC.presence_of_element_located(locator))
            return self.wait(timeout).until(EC.presence_of_all_elements_located(locator))
        except:
            assert False, f'Элемента {locator} на странице не обнаружено '

    def click(self, locator, timeout=1):
        for i in range(RETRY_COUNT):
            try:
                self.find(locator)
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                return
            except StaleElementReferenceException:
                if i < RETRY_COUNT - 1:
                    pass
        raise

    def scroll_to_element(self, element):
        self.driver.execute_script('arguments[0].scrollIntoView(true);', element)

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 3
        return WebDriverWait(self.driver, timeout=timeout)

    def authorization(self, user, password):
        user_field = self.find(self.locators.INPUT_NAME)
        user_field.clear()
        password_field = self.find(self.locators.INPUT_PASSWORD)
        password_field.clear()
        password_field.send_keys(password)
        user_field.send_keys(user)
        self.find(self.locators.AUTHORIZATION_BUTTON).click()

    def form_valid_user_data(self):
        username = fake.last_name()
        while len(username) not in range(7, 16):
            username = fake.last_name()

        password = fake.password()
        email = fake.email()

        return {"username": username, "password": password, "email": email}
