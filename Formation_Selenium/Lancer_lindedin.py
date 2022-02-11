import imp
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.com")
time.sleep(5)
driver.maximize_window()
time.sleep(3)

sh_element = driver.find_element(By.NAME,"q")
shh_element = driver.find_element(By.CLASS_NAME,"CcAdNb")
sh_element.clear()

sh_element.send_keys("linkedin")
sh_element.send_keys(Keys.ENTER)

time.sleep(3)
lk_elm = driver.find_element(By.CSS_SELECTOR, "#rso > div:nth-child(1) > div > div > div > div > div > div > div.yuRUbf > a > h3")
lk_elm.click()

co_btn = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
co_btn.click()

time.sleep(3)
id_elm = driver.find_element(By.ID, "username")
id_elm.send_keys("jean.martinos20@gmail.com")

time.sleep(1)
pwd_elm = driver.find_element(By.ID, "password")
pwd_elm.send_keys("b&")

time.sleep(1)
btn_elm = driver.find_element(By.CSS_SELECTOR, "#organic-div > form > div.login__form_action_container > button")
btn_elm.click()