
#https://www.pythontutorial.net/python-unit-testing/python-unittest/
#https://docs.python.org/3/library/unittest.html

"""
    -----------------------------------
    INDICE
    ------------------------------------
    Unitest basics
    Test fixtures               setUp() / setUpClass() / setUpModule()
    unittest.main()
    Assert methods (UnitTest)
    Skiptest
    Run test
    Test suites 
    Organize test
    Covertura del test (% testeado de un proyecto
    
    >>Mock/patch
    >>Stub
    >>Parameterized tests    subTest()
    
    >>Reports
"""

"""-------------------------------------------------------
    Unittest (PyTest)
-------------------------------------------------------"""
"""
    Test Fixture    Metodos setUp(self)/tearDown(self). Methods that execute before and after a test method executes. 
    Assertions      Methods that check the behavior of the component being tested.
    Test case       Metodo/Funcion a probar ///unittest.TestCase()
    Test Suite      A group of related tests executed together. Coleccion de test case ///unittest.TestSuite()
    Test runner     Programa que ejecuta los test case/suites
    Test report     resporte del test
"""   
 
"""   
UnitTest basics

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
            verbosity = 2)                                                                      #<---- Get more info on the result from UnitTest  

#NOTA:   Nombre de clase     Test...
#        Nombre de metodos   def test_...
#---------------------------------------------------------


"""----------------------------------------
    Test fixtures setUpClass() / setUpModule()
-------------------------------------------
Los metodos setUp() and  tearDown() de clase heredada de unittest.TestCase, se aplican en cada metodo de la clase.  Abren y cierran en cada uno de los test cases (metodos)
Para correr todos los test cases de una clase de una sola vez sin cerrar la prueba, usar los Test Fixtures de la clase padre.
Pada correr todos los test cases de todas las clases de manera corrida usar setUpModule() and  tearDownModule()

setUp() and  tearDown() runs before and after EVERY test method in the test class.
setUpClass() and tearDownClass() runs before and after ALL test methods of a class. (requiere decorador para metodo de padre classmethod)
setUpModule() and tearDownModule() are function runs before and after all the test methods in that module.py, (go outside the class).
"""

import unittest

class Test(unittest.TestCase):
    @classmethod                                                            #<---- Decorador para llamar metodo de padre
    def setUpClass(cls):                                                    #<---- setUp >>> setUpClass
        cls.driver = webdriver                                              #<----  self. >>> cls.
        
    @classmethod                                                            #<---- Decorador para llamar metodo de padre
    def tearDownClass(cls):                                                 #<---- tearDown >>>> tearDownClass
        cls.driver.quit()                                                   #<----  self. >>> cls.

#-----------------------------------------------------------------------------------------------------------

import unittest

def setUpModule():
    pass
def tearDownModule():
    pass

class Test(unittest.TestCase):
    def test_case_1(self):
        pass
    def test_case_2(self):
        pass


"""----------------------------------------
    unittest.main()
-------------------------------------------"""
""" A command-line program that loads a set of tests from module and runs them; this is primarily for making test modules conveniently executable.
Esta función imprimirá un informe de resultados incluyendo el tiempo total de ejecución, el número de pruebas ejecutadas, 
el número de pruebas correctas, el número de errores y el número de pruebas fallidas. Sin el, el resultado de la prueba se emitirá sin resumen.
The simplest use for this function is to include the following line at the end of a test script:"""
if __name__ == '__main__':
    unittest.main()
    
# Argumentos unitest.main
unittest.main(
    module='__main__', 
    defaultTest=None, 
    argv=None, 
    testRunner=None, 
    testLoader=unittest.defaultTestLoader, 
    exit=True, 
    verbosity=1,                                    #run tests with more detailed information if set: verbosity=2
    failfast=None, 
    catchbreak=None, 
    buffer=None, 
    warnings=None)



The defaultTest argument is either the name of a single test or an iterable of test names to run if no test names are specified via argv. If not specified or None and no test names are provided via argv, all tests found in module are run.

The argv argument can be a list of options passed to the program, with the first element being the program name. If not specified or None, the values of sys.argv are used.

The testRunner argument can either be a test runner class or an already created instance of it. By default main calls sys.exit() with an exit code indicating success or failure of the tests run.

The testLoader argument has to be a TestLoader instance, and defaults to defaultTestLoader.

main supports being used from the interactive interpreter by passing in the argument exit=False. This displays the result on standard output without calling sys.exit():

    from unittest import main
    main(module='test_module', exit=False)
    
The failfast, catchbreak and buffer parameters have the same effect as the same-name command-line options.

The warnings argument specifies the warning filter that should be used while running the tests. If it’s not specified, it will remain None if a -W option is passed to python (see Warning control), otherwise it will be set to 'default'.

Calling main actually returns an instance of the TestProgram class. This stores the result of the tests run as the result attribute.




"""-----------------------------------------------------
Assert methods (UnitTest)
-----------------------------------------------------"""
"""Assert methods of the TestCase class"""            
## X = resultado a testear // Y = con lo que se comparara/resultado esperado  // MSG = (Opc/str) texto que aparacera si Fail

assertEqual(x, y, msg=None)	            # x == y
assertNotEqual(x,y,msg=None)	        # x != y
assertTrue(x, msg=None)	                # bool(x) is True
assertFalse(x, msg=None)	            # bool(x) is False
assertIs(x, y , msg=None)	            # x is y (verificar si es el mismo objeto)
assertIsNot(x, y, msg=None)	            # x is not y (verificar si no es el mismo objeto)
assertIsNone(x, msg=None)	            # x is None
assertIsNotNone(x , msg=None)	        # x is not None
assertIn(x, y, msg=None)	            # x in y
assertNotIn(x, y, msg=None)	            # x not in y
assertIsInstance(x, y, msg=None)	    # isinstance(x, y) x es instancia de la clase y
assertNotIsInstance(x, y, msg=None)	    # not isinstance(x, y)  x no es instancia de la clase y
assertGreater(x, y)	                    # x > y
assertGreaterEqual(x, y)	            # x >= y
assertLess(x, y)	                    # x < y
assertLessEqual(x, y)	                # x <= y

assertAlmostEqual(first, second, places=7, msg=None, delta=None)	            # round(x-y, 7) == 0
assertNotAlmostEqual(first, second, places=7, msg=None, delta=None)	            # round(x-y, 7) != 0
assertRegex(s, r)	                    # r.search(s)
assertNotRegex(s, r)	                # not r.search(s)
assertCountEqual(x, y)	                # x and y have the same number of elements in the same number.

#ej-----------------------------------------
import unittest
from moduloX import Widget

class TestCaseWidget(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50,50), 'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150), 'wrong size after resize')
#-------------------------------------------


"""Assert methods that check exceptions / warnings / log messages """

with self.assertRaises(Excetiondesired):         #Evalua que la funcion raise del objeto testeado efectivamente levante un exception. Sino lo levanta es un fail.

#ej-----------------------------------------

    def test_length_with_wrong_type(self):          
        with self.assertRaises(TypeError):          #<-- TypeError = Error para tipo de valor float/string/int/etc... Square lo tiene en su codigo.
            square = Square('bab')                  #<-- Valor es string y leng esperaba int/float.

# -------------------------------------------

assertRaises(exc, fun, *args, **kwds)	        # fun(*args, **kwds) raises exc
assertRaisesRegex(exc, r, fun, *args, **kwds)	# fun(*args, **kwds) raises exc and the message matches regex r
assertWarns(warn, fun, *args, **kwds)	        # fun(*args, **kwds) raises warn
assertWarnsRegex(warn, r, fun, *args, **kwds)	# fun(*args, **kwds) raises warn and the message matches regex r
assertLogs(logger, level)	                    # The with block logs on logger with a minimum level
assertNoLogs(logger, level)	                    # The with block does not log on logger with a minimum level




"""-----------------------------------------------------
Skip test
-----------------------------------------------------"""

@unittest.skip()                                    #<--- Skip un test case(test method) o Skip toda una clase.
@unittest.skip('text a mostrar')

#ej.----------------------------------

class TestDemo(unittest.TestCase):                  #
    @unittest.skip('Work in progress')              #<---- Skipea solo el caso 1 y corre los demas
    def test_case_1(self):                          #
        self.assertEqual(1+1, 2)                    #
    
    
@unittest.skip('Work in progress')                  #<---- Skipea todos los casos de la clase
class TestDemo(unittest.TestCase):                  #
    def test_case_1(self):                          #
        self.assertEqual(1+1, 2)                    #

#-------------------------------------


@unittest.skipIf(condition, "text reason")          #<---- Salta test si cumple una condicion
@unittest.skipUnless(condition, "text reason")      #<---- Salta test a menos que cumpla una condicion
#ej----------------------------------------
from sys import platform

class TestDemo(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(1+1, 2)
        
    @unittest.skipIf(platform.startswith("win"), "Do not run on Windows")   #<-- Saltara case 2 si es windows la plataforma
    def test_case_2(self):
        self.assertIsNotNone([])



"""-----------------------------------------------------
Test suites    https://docs.python.org/3/library/unittest.html
-----------------------------------------------------"""
"""group tests together according to the features they test."""

# Everything 
python -m unittest discover -v                  #<--  run all tests in the test directory, (from the project folder). 
                                                #         discover is a subcommand that finds all the tests in the project.
# Single module
python -m unittest paquete.module -v      

# Single test class
python -m unittest paquete.module.testclass -v 
    
# Single test method
python -m unittest paquete.module.testclass.testmethod -v

#customized test suite



"""-----------------------------------------------------
Test suites    https://docs.python.org/3/library/unittest.html
-----------------------------------------------------"""
"""
Group tests together according to the features they test.
    1.- Import modules
    2.- create a object from TestSuite class (unittest.TestSuite)
    3.- add test cases 
    4.- Run the suite with the desired test cases
"""

def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_default_widget_size'))
    suite.addTest(WidgetTestCase('test_widget_resize'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())



"""----------------------------------
    Organize test
---------------------------------"""
"""
Project
    ├── shapes
    |  ├── circle.py
    |  ├── shape.py
    |  └── square.py
    └── test                        <<<<<<
        ├── test_circle.py
        ├── test_square.py
        └── __init__.py
"""


"""----------------------------------
    Test coverage
---------------------------------"""
"""Test coverage is the porcentage of lines executed by test cases of the script base"""

python -m coverage run -m unittest      # 1o. generate the coverage data
python -m coverage report               # 2o. turn the coverage data into a report
python -m coverage html                 # 3o. generate the coverage report in HTML format



"""----------------------------------
    Still not done
---------------------------------"""
"""
Mock                                    use the Mock (mimic) class to mimic behaviors of another function or class
        unittest.mock
        unittest.mock.MagicMock

patch()                                 temporarily replace an object with another object for testing         
        unittest.mock.patch()
        
Stub                                    return hard-coded values for testing.

Mocking requests module                 mock the requests module to test an API call using the unittest module

"""

"""--------------------------------------
Parameterized tests          subTest()
-----------------------------------------"""
"""
By using the subTest() context manager, the test do not stop after the first failure. 
Also, it shows a very detailed message after each failure so that you can examine the case.
"""


"""--------------------------------------
Tests Report          HTMLTestRunner
-----------------------------------------"""

#1.- Instalar Reportador
pip install html-testRunner 

#2.- Codigo test runner 
from HtmlTestRunner import HTMLTestRunner

if __name__ == "__main__":                                          
        unittest.main(                                                                          #<---- unittest.main() to run unitest in the call
            testRunner = HTMLTestRunner(                                                        #<---- Creacion de reporte con TestRuner de PyUnitReport. output = carpeta, report_name = nombre de html con el reporte
                output = 'report',                                                 
                report_name = 'test-report'))


#Report test suites ?????

#2.- Codigo test runner 
kwargs = {
    "output": "reports/smoke-report",
    "report_name": "smoke-report",
    "combine_reports": True,
    "add_timestamp": False
}

# ? create runner with the parameters and run
runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)