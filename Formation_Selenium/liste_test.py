

from logging import raiseExceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import string
from selenium.webdriver.support.ui import WebDriverWait								
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

"Se rendre sur le site web"
driver = webdriver.Chrome()
time.sleep(1)
driver.maximize_window()
driver.maximize_window()
driver.get("http://demostore.supersqa.com/")
time.sleep(2)

liste_choix = driver.find_element(By.NAME, "orderby").click
# import pdb; pdb.set_trace()

choix = driver.find_element(By.CSS_SELECTOR, "#main > div:nth-child(2) > form > select > option:nth-child(2)").click
# print(choix(2).text)

