from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import unittest

class HomePage(unittest.TestCase):

    def setUp(self):
        self.serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.serv_obj)
        self.driver.get("https://zoro.to/")
        

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()