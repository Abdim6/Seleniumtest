from asyncio import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import string
from selenium.webdriver.support.ui import WebDriverWait								
from selenium.webdriver.support import expected_conditions as EC 
import test_driver

def sedeconnecter():
    # driver = webdriver.Chrome()

    driver = test_driver.driver
    "se rendre sur la page de mon compte"
    myaccount_btn = driver.find_element(By.XPATH, '//*[@id="site-navigation"]/div[1]/ul/li[4]/a')
    myaccount_btn.click()
    time.sleep(2)
    
    "Deconnexion" 
    "Vérification de la deconnexion"       
    # wait = WebDriverWait(driver,10)
    # deco_btn = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="post-9"]/div/div/nav/ul/li[6]/a')))	
    deco_btn = driver.find_element(By.XPATH,'//*[@id="post-9"]/div/div/nav/ul/li[6]/a')	
    deco_btn.click()	
    time.sleep(2)
    print("La deconnexion s'est bien passée")
    driver.quit()