from selenium.webdriver.common.by import By

class MainPageLocators(object):
    FULLSITE_BUTTON = (By.XPATH, '//*[@id="action-button"]/a')
    INPUT_FIELD = (By.NAME, "keyword")

class HomePageLocators(object):
    LOGIN_BUTTON = (By.XPATH, '//*[@id="header_right"]/div/a')
    SECOND_LOGIN_BUTTON = (By.ID, 'btn-login')
    CAPTCHA_BOX = (By.CSS_SELECTOR, ".recaptcha-checkbox-border")
    SEARCH_BUTTON = (By.XPATH, '//*[@id="mobile_search"]/i')
    SECOND_SEARCH_BUTTON = (By.XPATH, '//*[@id="search"]/div/form/button/i')
    ADD_LIST = (By.XPATH, '//*[@id="watch-list-content"]/a')
    ADD_LIST_PLANNED = (By.XPATH, '//*[@id="watch-list-content"]/div/a[3]')
    PROFILE_BUTTON = (By.XPATH, '//*[@id="user-slot"]/div/div/div[1]/div/img')
    WATCHLIST_BUTTON = (By.XPATH, '//*[@id="user_menu"]/div[2]/a[3]')
    EDIT_LIST = (By.XPATH, '//*[@id="main-wrapper"]/div[2]/div[1]/div/div[3]/div[1]/div/div[1]/a')
    REMOVE_LIST = (By.XPATH, '//*[@id="main-wrapper"]/div[2]/div[1]/div/div[3]/div[1]/div/div[1]/div/a[6]')
    