from lib2to3.pgen2 import driver
from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get("http://demostore.supersqa.com/")

mon_btn = driver.find_element(By.ID, "site-header-cart")
mon_btn.click()