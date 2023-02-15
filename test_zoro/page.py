from locator import *
from element import BasePageElement
from selenium.webdriver.common.keys import Keys

class SearchTextElement(BasePageElement):
    locator = "keyword"

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    search_text_element = SearchTextElement()

    def is_title_matches(self):
        return "Watch Anime Online, Free Anime Streaming Online on Zoro.to Anime Website" in self.driver.title
    
    def click_fullsite_button(self):
        element = self.driver.find_element(*MainPageLocators.FULLSITE_BUTTON)
        element.click()
    
    def click_search_button(self):
        element = self.driver.find_element(*MainPageLocators.INPUT_FIELD)
        element.send_keys(Keys.ENTER)

class SearchResultPage(BasePage):

    def is_results_found(self):
        return "Blue Lock" in self.driver.page_source