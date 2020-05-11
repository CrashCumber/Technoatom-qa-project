from selenium.webdriver.common.by import By


class BaseLocators:
    INPUT_NAME = (By.XPATH,  '//input[@name="username"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@name="password"]')
    AUTHORIZATION_BUTTON = (By.XPATH, '//input[@type="submit" and @value="Login"]')
    CREATE_ACCOUNT_BUTTON = (By.PARTIAL_LINK_TEXT, 'Create an account')
    INVALID_DIV = (By.XPATH, '//div[contains(text(),"Invalid username or password")]')
    INVALID_LENGTH_DIV = (By.XPATH, '//div[contains(text(),"Invalid username or password")]')
    LOGIN_CONTROL_DIV = (By.ID, 'login-controls')



class RegPageLocators(BaseLocators):
    INPUT_NEW_NAME = (By.XPATH,  '//input[@name="username"]')
    INPUT_NEW_PASSWORD = (By.XPATH, '//input[@name="password"]')
    INPUT_EMAIL = (By.XPATH, '//input[@name="email"]')
    INPUT_REPEAT_PASSWORD = (By.XPATH, '//input[@name="confirm"]')
    CHECK_BOX = (By.XPATH, '//input[@name="term"]')
    REGISTER_BUTTON = (By.XPATH, '//input[@type="submit" and @value="Register"]')
    INVALID_EMAIL_DIV = (By.XPATH, '//div[contains(text(),"Invalid email address')
    INVALID_NAME_DIV = (By.XPATH, '//div[contains(text(),"Incorrect username length")]')


class MainPageLocators(BaseLocators):
    LOGOUT_BUTTON = (By.XPATH,  '//a[contains(text(),"Logout")]')
    LOG_INFO_DIV = (By.ID, 'login-controls')
    LOG_VK_ID = (By.XPATH,  '//li[contains(text(),"VK ID:")]')
    LOG_USERNAME = (By.XPATH,  '//li[contains(text(),"Logged as")]')


    API_BUTTON = (By.XPATH, '//a[@href="https://en.wikipedia.org/wiki/Application_programming_interface"]')
    FUT_INTERNET_BUTTON = (By.XPATH, '//a[@href="https://www.popularmechanics.com/technology/infrastructure/a29666802/future-of-the-internet/"]')
    SMTP_BUTTON = (By.XPATH, '//a[@href="https://ru.wikipedia.org/wiki/SMTP"]')

    FACT_PYTHON_DIV = (By.XPATH, '//div[contains(@class,"uk-text-large")]/p[2]')

    HOME_BUTTON = (By.XPATH, '//a[contains(text(),"Home")]')

    PYTHON_BUTTON = (By.XPATH, '//a[text()="Python"]')
    PYTHON_HISTORY_BUTTON = (By.XPATH, '//a[text()="Python history"]')
    FLASK_BUTTON = (By.XPATH, '//a[text()="About Flask"]')

    NETWORK_BUTTON = (By.XPATH, '//a[contains(text(),"Network")]')
    NEWS_BUTTON = (By.XPATH, '//a[contains(text(),"News")]')
    DOWNLOAD_BUTTON = (By.XPATH, '//a[text()="Download"]')
    TCPEXAMP_BUTTON = (By.XPATH, '//a[contains(text(),"Examples ")]')

    LINUX_BUTTON = (By.XPATH, '//a[contains(text(),"Linux")]')
    CENTOS_BUTTON = (By.XPATH, '//a[contains(text(),"Download Centos7")]')




