
https://www.pythontutorial.net/python-unit-testing/python-unittest/

    -------------------------------------------------------
    Unittest (PyTest)
    -------------------------------------------------------
    Test Fixture    Metodos. Methods that execute before and after a test method executes. Preparan el ambiente de test
    Assertions      Methods that check the behavior of the component being tested.
    Test case       Metodo/Funcion a probar
    Test Suite      A group of related tests executed together. Coleccion de test case
    Test runner     Programa que ejecuta los test case/suites
    Test report     resporte del test


    Ejemplo UnitTest/Selenium  
    ---------------------------------------------------------   
    class TestWebpage(unittest.TestCase):                                                           #<---- Crea objeto que hereda de TesCase class que tiene como metodos los test fixture and test cases

        def setUpClass(cls):                                                                        #<---- Test Fixture. Prepara lo requerido antes del test.
            cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))   
            

        def test_visit_wikipedia(self):                                                             #<---- Pruebas Unitarias / cada test case
            self.driver.get('https://www.wikipedia.org')  

        def test_...


        def tearDownClass(cls):                                                                     #<---- Test Fixture. Preparado para dictar como culminar
            cls.driver.quit()                                                         

        if __name__ == "__main__":                                          
            unittest.main(                                                                          #<---- unittest.main() to run unitest in the call
                verbosity = 2,                                                                      #<---- Get more info on the result from UnitTest
                testRunner = HTMLTestRunner(                                                        #<---- Creacion de reporte con TestRuner de PyUnitReport. output = carpeta, report_name = nombre de html con el reporte
                    output = 'report',                                                 
                    report_name = 'test-report'))  

    NOTA:   Nombre de clase     Test...
            Nombre de metodos   def test_...
    ---------------------------------------------------------




Section 2. assert methods
This section covers the assert methods so that you know how to each of them more effectively.

assert methods – introduce to you a brief overview of the assert methods of the TestCase class.
assertEqual() – test if two values are equal.
assertAlmostEqual() – test if two values are approximately equal.
assertIs() – test if two objects are the same.
assertIsInstance() – test if an object is an instance of a class or a tuple of classes.
assertIsNone() – test if an expression is None.
assertTrue() – test if an expression is True.
assertIn() – test if a member is in a container.

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