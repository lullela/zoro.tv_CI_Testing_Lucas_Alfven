from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import page
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class StartPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        
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
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.driver.get("https://zoro.to/home")
        cls.driver.implicitly_wait(5)
        homePage = page.HomePage(cls.driver)
        homePage.click_login_button()
        homePage.login_user_element = "lulle-99@hotmail.com"
        homePage.login_password_element = "TestAutomation99"
        #Captcha förhindrar automatisering, manuell start
        input("CLICK THE CAPTCHA AND LOGIN THEN PRESS ENTER")
        WebDriverWait(cls.driver, 10).until(EC.url_contains("https://zoro.to/home"))
        cls.auth_cookie = cls.driver.get_cookie("auth")
        if cls.auth_cookie:
            cls.driver.add_cookie(cls.auth_cookie)
            cls.driver.refresh()
        # cls.driver.maximize_window()
    
    def setUp(self):
        self.driver.get("https://zoro.to/home")
        if hasattr(self, "auth_cookie") and self.auth_cookie is not None:
            cookie_dict = {
                'name': self.auth_cookie['name'],
                'value': self.auth_cookie['value'],
                'domain': self.auth_cookie['domain'],
                'path': self.auth_cookie['path'],
                'expiry': self.auth_cookie['expiry']
            }
            self.driver.add_cookie(cookie_dict)

    def test_valid_login(self):
        homePage = page.HomePage(self.driver)
        homePage.is_correct_login()
    
    def test_add_to_list(self):
        homePage = page.HomePage(self.driver)
        homePage.click_home_search_button()
        homePage.search_text_element = "Blue Lock"
        homePage.click_home_2_search_button()
        homePage.click_serie_title()
        homePage.add_to_list()
        homePage.go_to_watchlist()
        search_result_page = page.SearchResultPage(self.driver)
        search_result_page.is_results_found()
    
    def test_remove_from_list(self):
        homePage = page.HomePage(self.driver)
        homePage.go_to_watchlist()
        homePage.remove_from_list()
        search_result_page = page.SearchResultPage(self.driver)
        self.assertFalse(search_result_page.is_results_found())
   
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()