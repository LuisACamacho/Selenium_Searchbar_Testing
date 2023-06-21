import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from selenium.webdriver.common.by import By 




class GoogleSearch(unittest.TestCase):
    driver = webdriver.Chrome()
    @classmethod
    def setupClass(cls):
        
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
     
    def test_search_automationstepbystep(self):
       
        self.driver.get('https://www.google.com')
        time.sleep(1)   #sleep was used in tests since elements were not loaded and cause tests to fail 
        self.driver.find_element(By.XPATH,'//textarea[@name="q"]').send_keys("Automation Step by Step")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR,'[name = "btnK"]').click()
       

    def test_search_SDLC(self):
        
        self.driver.get('https://www.google.com')
        time.sleep(1)
        self.driver.find_element(By.XPATH,'//textarea[@name="q"]').send_keys("SDLC")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR,'[name = "btnK"]').click()
      

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output= 'C:/Users/angel/Selenium Projects/Selenium_python_1/Reports'))













