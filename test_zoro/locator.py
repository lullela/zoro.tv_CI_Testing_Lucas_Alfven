from selenium.webdriver.common.by import By

class MainPageLocators(object):
    FULLSITE_BUTTON = (By.XPATH, '//*[@id="action-button"]/a')
    INPUT_FIELD = (By.NAME, "keyword")

class SearchResultsPageLocators(object):
    pass