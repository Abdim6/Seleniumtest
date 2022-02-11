"Utilisé cette ligne de commande pour installer le webdriverChrome"
# xattr -d com.apple.quarantine /Users/amahmoud/Downloads/chromedriver

from multiprocessing.connection import wait
from selenium.webdriver.common.keys import keys
from sys import executable
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pdb
import time
from selenium.webdriver.support.ui import Select


"Methode 1 avec la version 3"
# driver = webdriver.Chrome(executable_path="/Users/amahmoud/Downloads/chromedriver")
# driver.get("https://google.com")


"Methode 1 avec la version 4"
# se = Service(executable_path="/Users/amahmoud/Downloads/chromedriver")
# driver = webdriver.Chrome(service=se)
# driver.get("https://google.com")


"Methode 2 avec la version 4 : is adding the exécutable to system path"
driver = webdriver.Chrome()
driver.get("http://demostore.supersqa.com/")

el = driver.find_element(By.ID, "site-header-cart")
el.click()
el1 = driver.find_element(By.XPATH, '//*[@id="site-navigation"]/div[1]/ul/li[4]')
el1.click()

time.sleep(15)
driver.quit()


"Saisir un champ"
u_name.send_keys('abcd')

"clique enter quand tu es dans le champs recherche"
search_field.send_keys(keys.ENTER)
"ou utiliser la tabulation"
search_field.send_keys(keys.TAB)

"Avec une liste deroulante"
dropdown_obj = select(my_dropdown)
"=> avec pdb : dir(dropdown_obj) tu peux afficher comme d'hab la liste des methode qu'on peut utiliser"
dropdown_obj.all_selected_option[0].text 
dropdown_obj.select_by_index(2) 


"trop fort : il y'a la possibilité d'afficher la liste déroulante dans la console"
for option in dropdown_obj.option: print(option.text)

"Pour le checkbox"
mon_choix = driver.find_element()
mon_choix.click()
assert mon_choix.is_selected(), f"after clicking value {to_select_value} it is not selected"

"Savoir le nb de checkbox"
all_checkboxes = driver.find_elements()
assert len(all_checkboxes)==nb, "Si non erreur, cas de non égalité"

"exception"
raise Exception(f"lkjfkfhkd")