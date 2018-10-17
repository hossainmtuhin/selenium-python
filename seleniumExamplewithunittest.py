import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GoogleSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("D://Tuhin_Backup//software_//automation_//selenium webdriver tools//chromedriver_win32//chromedriver.exe")


    def test_search_in_googl(self):
        driver = self.driver
        driver.get("https://google.com")    
        self.assertIn("Google", driver.title)
        element = driver.find_element_by_name("q")
        element.send_keys("test")
        element.send_keys(Keys.RETURN)
        
        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)        

