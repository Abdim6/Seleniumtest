"Ce fichier a pour but uniquement de lancer le navigateur "

from selenium import webdriver
import time


"Se rendre sur le site web"
driver = webdriver.Chrome()
time.sleep(1)
driver.maximize_window()
driver.get("http://demostore.supersqa.com/")
time.sleep(2)