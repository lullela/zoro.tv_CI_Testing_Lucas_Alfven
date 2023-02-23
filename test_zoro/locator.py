from selenium.webdriver.common.by import By

class MainPageLocators(object):
    FULLSITE_BUTTON = (By.XPATH, '//*[@id="action-button"]/a')
    INPUT_FIELD = (By.NAME, "keyword")

class HomePageLocators(object):
    LOGIN_BUTTON = (By.XPATH, '//*[@id="header_right"]/div/a')
    SECOND_LOGIN_BUTTON = (By.ID, 'btn-login')
    CAPTCHA_BOX = (By.CSS_SELECTOR, ".recaptcha-checkbox-border")