# Importaciones 
### Librerias que gustes usar ##############
import unittest                                                           
from pyunitreport import HTMLTestRunner                              
import time

### Driver #################################
from selenium import webdriver                                          #<---- Importar driver especifico para web en donde se realizara test 
from selenium.webdriver.chrome.service import Service as ChromeService            #<-- (Este para Chrome)
from webdriver_manager.chrome import ChromeDriverManager


class TestName(unittest.TestCase):                                    #<---- Crear clase para un Test case (/Unittest)
    
    @classmethod                                                            #<---- Decorador (multiples test - una sola pagina)
    def setUpClass(cls):                                                    #<---- Inicializa Test (Test Fixture/Unittest)
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))    #<---Instala Driver de Browser. Asigna Driver a variable driver. 
        time.sleep(2)

    def test_visit_wikipedia(self):                                     #<----Pruebas Unitarias a realizar (inician siempre con test_ (buena practica))
        self.driver.get('https://www.wikipedia.org')                              #<--Abrir Webpage
        time.sleep(2)

    @classmethod                                                            #<---- Decorador (multiples test - una sola pagina)
    def tearDownClass(cls):                                                 #<---- Instrucciones para finalizacion de la prueba (Test Fixture/Unittest)
        cls.driver.quit()                                                         #<--cierra Webpage


if __name__ == "__main__":                                          #<---- Name de la clase (iniciar codigo desde consola)
    unittest.main(                                                
        verbosity = 2,                                            
        testRunner = HTMLTestRunner(                                    #<---- Llamar a TestRuner para generar reporte de prueba
            output = 'report',                                                 #<-- Carpeta del reporte
            report_name = 'test-report')                                #<-- Nombre del reporte
            )
