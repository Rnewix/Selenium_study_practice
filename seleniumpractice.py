# Importaciones 
import unittest                                                           
from HtmlTestRunner import HTMLTestRunner                              
import time

#Selenium driver 
from selenium import webdriver                                          
from selenium.webdriver.chrome.service import Service as ChromeService            
from webdriver_manager.chrome import ChromeDriverManager


class BlogSmogTest(unittest.TestCase):                                    
#Check if the page is able to be tested
    @classmethod                                                            
    def setUpClass(cls):                                                     
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))    
        time.sleep(2)
            
            
    def test_open_blog(self):                                     
        #Check if the web page can be open
        self.driver.get('http://127.0.0.1:8000/')                              
        time.sleep(2)

    @classmethod                                                            
    def tearDownClass(cls):                                                 
        cls.driver.quit()                                                         


if __name__ == "__main__":                                          
    unittest.main(                                                
        verbosity = 2,                                            
        testRunner = HTMLTestRunner(                                    
            output = 'report',                                                 
            report_name = 'test-report')                                
            )
