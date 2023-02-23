from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import unittest
import page


class StartPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=serv_obj)
        # cls.driver.implicitly_wait(5)
        # cls.driver.maximize_window()

    def setUp(self):
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
        self.driver.delete_all_cookies()
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    
class HomePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=serv_obj)
        cls.driver.implicitly_wait(5)
        # cls.driver.maximize_window()
    
    def setUp(self):
        self.driver.get("https://zoro.to/home")

    #Captcha kan förhindra automatiseringen här
    def test_valid_login(self):
        homePage = page.HomePage(self.driver)
        homePage.click_login_button()
        homePage.login_user_element = "lulle-99@hotmail.com"
        homePage.login_password_element = "TestAutomation99"
        homePage.click_captcha_box()
        homePage.click_second_login_button()
        homePage.is_correct_login()

    def tearDown(self):
        self.driver.delete_all_cookies()
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()