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
        self.driver.execute_script("arguments[0].click();", element)
    
    def click_search_button(self):
        element = self.driver.find_element(*MainPageLocators.INPUT_FIELD)
        element.send_keys(Keys.ENTER)

class HomePage(BasePage):

    def is_url_matches(self):
        return "https://zoro.to/home" in self.driver.current_url


class SearchResultPage(BasePage):

    def is_results_found(self):
        self.driver.find_element(By.LINK_TEXT, "Blue Lock")
    
    def is_results_empty(self):
        elements = self.driver.find_elements(By.CLASS_NAME, "film-poster-ahref")
        return len(elements) < 1