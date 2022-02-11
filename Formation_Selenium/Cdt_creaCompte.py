

from logging import raiseExceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import string
from selenium.webdriver.support.ui import WebDriverWait								
from selenium.webdriver.support import expected_conditions as EC 

"Generation des email"
letters = string.ascii_lowercase
rand_string = "".join(random.choice(letters) for i in range(15))
rand_mail = rand_string + "@gmail.com"


"Se rendre sur le site web"
driver = webdriver.Chrome()
time.sleep(1)
driver.maximize_window()
driver.maximize_window()
driver.get("http://demostore.supersqa.com/")
time.sleep(2)

myaccount_btn = driver.find_element(By.XPATH, '//*[@id="site-navigation"]/div[1]/ul/li[4]/a')
myaccount_btn.click()
time.sleep(2)

title_page = driver.title
print(title_page)
id_section = driver.find_element(By.ID,"reg_email")
pwd_section = driver.find_element(By.ID, "reg_password")
id_section.clear()
# id_section.send_keys("my_email")
id_section.send_keys(rand_mail)
pwd_section.send_keys("azerty1qrgqerge5")
time.sleep(3)


Submit_btn = driver.find_element(By.XPATH, '//*[@id="customer_login"]/div[2]/form/p[3]/button')

if Submit_btn.is_enabled()==True:
    Submit_btn.click()
    import pdb; pdb.set_trace()
    wait = WebDriverWait(driver,10)
    register_label = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'woocommerce-MyAccount-navigation')))	
    
    title_page2 = driver.title
    print(title_page2)
    print("PASS!")
else :
    print("Le bouton n'est pas actif")
    raise Exception("KO")


# print("PASS")

time.sleep(2)
driver.quit()