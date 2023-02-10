from selenium.webdriver.common.by import By

class MainPageLocators(object):
    FULLSITE_BUTTON = (By.XPATH, '//*[@id="action-button"]/a')
    SEARCH_BUTTON = (By.XPATH, '//*[@id="search-form"]/div/div/i')

class SearchResultsPageLocators(object):
    pass