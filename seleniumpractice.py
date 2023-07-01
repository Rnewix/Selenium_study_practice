# Importaciones 
import unittest                                                           
from HtmlTestRunner import HTMLTestRunner                              
import time

#Selenium driver 
from selenium import webdriver                                          
from selenium.webdriver.chrome.service import Service as ChromeService            
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

class BlogSmogTest(unittest.TestCase):                                    
#Check if the page is able to be tested
    @classmethod                                                            
    def setUpClass(cls):                                                     
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))    
        cls.driver.implicitly_wait(3)
            
    def test_open_blog(self):                                     
        #Check if the web page can be open
        try:
            self.driver.get('http://127.0.0.1:8000/')                              
        except: 
            raise WebDriverException('Web page no present/Server down')

    @classmethod                                                            
    def tearDownClass(cls):                                                 
        cls.driver.quit()                                                         


class HomeTest(unittest.TestCase):
# Check all element in test are present
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))    
        cls.driver.get('http://127.0.0.1:8000/') 
        cls.driver.implicitly_wait(3)
        
    def test_HomeNavBar_present(self):
        #Check if the the expected web elements are present and enable
        driver = self.driver
        driver.find_elements(By.ID, "navbar-main-header") 
        
    def test_Navbar_home_present(self):
        driver = self.driver
        navbarhome = driver.find_element(By.ID, "navbar-home") 
        navbarhome.is_displayed()
        navbarhome.is_enabled() 
    
    def test_Navbar_portfolio_present(self):
        driver = self.driver
        navbarportfolio = driver.find_element(By.ID, "navbar-portfolio") 
        navbarportfolio.is_displayed()
        navbarportfolio.is_enabled()

    @classmethod                                                            
    def tearDownClass(cls):                                                 
        cls.driver.quit()                                                         

if __name__ == "__main__":                                          
    unittest.main(                                                
        verbosity = 2,                                            
        testRunner = HTMLTestRunner(                                    
            output = 'report',                                                 
            report_name = 'Test-Report')                                
            )