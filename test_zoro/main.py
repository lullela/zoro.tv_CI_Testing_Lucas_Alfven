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

    #Uppdatera allt igen
    def test_title(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
    
    def test_search_bluelock(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "Blue Lock"
        mainPage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()
    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()