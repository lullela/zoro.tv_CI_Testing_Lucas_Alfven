from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import unittest
import page


class HomePage(unittest.TestCase):

    def setUp(self):
        self.serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.serv_obj)
        self.driver.get("https://zoro.to/")

    def test_title(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
    
    def test_search_bluelock(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "Blue Lock"
        mainPage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)
        search_result_page.is_results_found()
    
    def test_search_no_results(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "zaza"
        mainPage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)
        self.assertTrue(search_result_page.is_results_empty())

    def test_fullsite_home(self):
        mainPage = page.MainPage(self.driver)
        mainPage.click_fullsite_button()
        homePage = page.HomePage(self.driver)
        homePage.is_url_matches()
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()