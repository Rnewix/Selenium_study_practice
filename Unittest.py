
#https://www.pythontutorial.net/python-unit-testing/python-unittest/
#https://docs.python.org/3/library/unittest.html

"""-------------------------------------------------------
    Unittest (PyTest)
-------------------------------------------------------"""
"""
    Test Fixture    Metodos setUp(self)/tearDown(self). Methods that execute before and after a test method executes. 
    Assertions      Methods that check the behavior of the component being tested.
    Test case       Metodo/Funcion a probar
    Test Suite      A group of related tests executed together. Coleccion de test case
    Test runner     Programa que ejecuta los test case/suites
    Test report     resporte del test
"""   
 
"""   
UnitTest

The basic unit testing are the test cases (single scenarios that must be set up and checked for correctness (with asserts))
In unittest, test cases are represented by unittest.TestCase instances:          
    ------------------------------------------------------   
    class TestCasetWidgetSize (unittest.TestCase):
        def test_widget_size(self):
            widget = Widget('The widget')
            self.assertEqual(widget.size(), (50, 50))
    ------------------------------------------------------

    setUp()
        Tests can be numerous, and their set-up can be repetitive. To create and run multiples test
        we can use method setUp(), and the framework will automatically call for every single test.
    tearDown() 
        Method that tidies up after a testcase (test method) has been run

    setUp(), tearDown(), and __init__() will be called once per test and a new TestCase instance is created.
    If setUp() is succeeded, tearDown() will be run everytimes whether the test method succeeded or not.    
        ------------------------------------------------------
        class TestWidget(unittest.TestCase):                                    #Single test case or test escenary
            def setUp(self):                                
                self.widget = Widget('The widget')

            def test_default_widget_size(self):                                 #testcase 1 (test method 1)
                self.assertEqual(self.widget.size(), (50,50),
                                'incorrect default size')

            def test_widget_resize(self):                                       #testcase 2 (test method 2)      
                self.widget.resize(100,150)
                self.assertEqual(self.widget.size(), (100,150), 'wrong size after resize')
            
            def tearDown(self):
                self.widget.dispose()
        --------------------------------------------------
"""

#Ejemplo UnitTest/Selenium  
#---------------------------------------------------------   
class TestWebpage(unittest.TestCase):                                                           #<---- Crea objeto que hereda de TesCase class que tiene como metodos los test fixture and test cases

    def setUp(self):                                                                        #<---- Test Fixture. Prepara lo requerido antes del test.
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))   
        

    def test_visit_wikipedia(self):                                                             #<---- Prueba Unitaria / test case
        self.driver.get('https://www.wikipedia.org')  

    def test_...                                                                                #<---- Prueba Unitaria / test case


    def tearDown(self):                                                                     #<---- Test Fixture. Preparado para dictar como culminar
        self.driver.quit()                                                         

    if __name__ == "__main__":                                          
        unittest.main(                                                                          #<---- unittest.main() to run unitest in the call
            verbosity = 2,                                                                      #<---- Get more info on the result from UnitTest
            testRunner = HTMLTestRunner(                                                        #<---- Creacion de reporte con TestRuner de PyUnitReport. output = carpeta, report_name = nombre de html con el reporte
                output = 'report',                                                 
                report_name = 'test-report'))  

#NOTA:   Nombre de clase     Test...
#        Nombre de metodos   def test_...
#---------------------------------------------------------


"""----------------------------------------
    @classmethod 
-------------------------------------------
Con clase heredada de unittest.TestCase, cada test case correra uno a uno (corre uno y cierra)
Para correr cada test case seguido por otro sin cerrar la prueba debemos aplicar directamente los Test Fixtures
de la clase padre. 
"""

@classmethod                                                            #<---- Decorador para llamar metodo de padre
def setUpClass(cls):                                                    #<---- setUp >>> setUpClass
    cls.driver = webdriver                                              #<----  self. >>> cls.
    
@classmethod                                                            #<---- Decorador para llamar metodo de padre
def tearDownClass(cls):                                                 #<---- tearDown >>>> tearDownClass
    cls.driver.quit()                                                   #<----  self. >>> cls.



"""-----------------------------------------------------
Assert methods
-----------------------------------------------------"""
# Assert methods of the TestCase class

assert methods          # introduce to you a brief overview of the assert methods of the TestCase class.
.assertEqual()           # test if two values are equal.
.assertAlmostEqual()     # test if two values are approximately equal.
.assertIs()              # test if two objects are the same.
.assertIsInstance()      # test if an object is an instance of a class or a tuple of classes.
.assertIsNone()          # test if an expression is None.
.assertTrue()            # test if an expression is True.
.assertIn()              # test if a member is in a container.


import unittest

class TestCaseWidget(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')


"""-----------------------------------------------------
Test suites    https://docs.python.org/3/library/unittest.html
-----------------------------------------------------"""

It is recommended that you use TestCase implementations to group tests together according to the features they test. 
unittest provides a mechanism for this: the test suite, represented by unittest’s TestSuite class. 
In most cases, calling unittest.main() will do the right thing and collect all the module’s test cases for you and execute them.
However, should you want to customize the building of your test suite, you can do it yourself:

def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_default_widget_size'))
    suite.addTest(WidgetTestCase('test_widget_resize'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())





Section 3. Test doubles
This section introduces to you the test doubles to decouple the system under test code from the rest of the system so that code can be tested in isolation.

Mock – learn how to use the Mock class to mimic behaviors of another function or class.
patch() – show you how to use the patch() to temporarily replace an object with another object for testing.
Stubs – show you how to use the MagicMock class & patch() to create stubs.
Mocking requests module – learn how to mock the requests module to test an API call using the unittest module.


Section 4. Test coverage & Parameterized tests
This section introduces you to the test coverage and how to define parameterized tests using the subTest() context manager.

Generating test coverage reports – learn about test coverage and how to generate the test coverage report using the coverage module.
Defining parameterized tests using subTest() – show you how to define parameterized tests using the unittest’s subTest() context manager.