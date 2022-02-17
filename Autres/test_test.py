# import logging 

# logging.basicConfig(filename="/Users/amahmoud/Documents/Selenium/Autres//test.log")

# logging.debug("This is debug message")
# logging.warning("This is warning message")
# logging.error("This is error message")


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.6play.fr")
time.sleep(5)
driver.maximize_window()
time.sleep(3)
print(driver.title)
driver.fullscreen_window()
time.sleep(5)
driver.quit()