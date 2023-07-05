# Importaciones 
import unittest                                                           
from HtmlTestRunner import HTMLTestRunner                              

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
            
    def test_Blog_open(self):                                     
        #Check if the web page can be open
        try:
            self.driver.get('http://127.0.0.1:8000/')                              
        except: 
            raise WebDriverException('Web page no present / Server down')
        
    def test_Home_Open(self):                                     
        #Check if the home page can be open
        try:
            self.driver.get('http://127.0.0.1:8000/')                              
        except: 
            raise WebDriverException('Home page cannot be opened / Server down')

    def test_Portfolio_open(self):                                     
        #Check if the Portfolio page can be open
        try:
            self.driver.get('http://127.0.0.1:8000/my_projects/')                              
        except: 
            raise WebDriverException('Portfolio page cannot be opened / Server down')

    def test_Aboutme_open(self):                                     
        #Check if the About me page can be open
        try:
            self.driver.get('http://127.0.0.1:8000/about_us/')                              
        except: 
            raise WebDriverException('About me page cannot be opened / Server down')

    def test_Contact_open(self):                                     
        #Check if the Contact page can be open
        try:
            self.driver.get('http://127.0.0.1:8000/contact/')                              
        except: 
            raise WebDriverException('Contact page cannot be opened /  Server down')

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
        
    def test_Navbar_home_presence(self):
        driver = self.driver
        navbarhome = driver.find_element(By.ID, "navbar-home") 
        assert navbarhome.is_displayed()
        assert navbarhome.is_enabled() 
    
    def test_Navbar_portfolio_presence(self):
        driver = self.driver
        navbarportfolio = driver.find_element(By.ID, "navbar-portfolio") 
        assert navbarportfolio.is_displayed()
        assert navbarportfolio.is_enabled()
    
    def test_Navbar_aboutme_presence(self):
        driver = self.driver
        navbaraboutme = driver.find_element(By.ID, "navbar-Aboutme") 
        assert navbaraboutme.is_displayed()
        assert navbaraboutme.is_enabled()

    def test_Navbar_contact_presence(self):
        driver = self.driver
        navbarcontact = driver.find_element(By.ID, "navbar-Contact") 
        assert navbarcontact.is_displayed()
        assert navbarcontact.is_enabled()
        
#    def test_home_h1_text(self):
#        driver = self.driver
#        homeh1 = driver.find_element(By.XPATH, "/html/body/div/main/h1") 
#        assert homeh1.is_displayed()
#        assert homeh1.text == "Roca Carlos Backend developer."
    
#    def test_home_description_text(self):
#        driver = self.driver
#        homedescription = driver.find_element(By.XPATH, "/html/body/div/main/p[1]/text()") 
#        assert homedescription.is_displayed()
#        assert homedescription.text == "I hope you to enjoy your visit in my first web page. Please check more about my work and my knowledge."   

    def test_Home_MainButton_presence(self):
        driver = self.driver
        mainbutton = driver.find_element(By.LINK_TEXT, "Learn more") 
        assert mainbutton.is_displayed()
        assert mainbutton.is_enabled()
    
#    def test_Home_footer(self):
#        driver = self.driver
#        homefooter = driver.find_element(By.XPATH, "/html/body/div/footer/p") 
#        assert homefooter.is_displayed()
#        assert homefooter.text == "©2022. All rights reserved."

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