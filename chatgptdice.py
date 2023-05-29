from selenium import webdriver  #importamos la libreria webdriver
from webdriver_manager.chrome import ChromeDriverManager 
 
driver = webdriver.Chrome(ChromeDriverManager().install())   #Descargamos el controlador
driver.get("http://www.google.com")   #abrimos una nueva ventana de Google Chrome

buscar = driver.find_element_by_name("q")  #Comenzamos nuestra búsqueda
buscar.send_keys("Que es la fotosintesis")  #Escribimos nuestra búsqueda
buscar.submit() #Hacemos click en el boton de buscar

driver.get('https://es.wikipedia.org/wiki/Fotos%C3%ADntesis')  #llegamos a la pagina de wikipedia donde nos dice que es la Fotosíntesis