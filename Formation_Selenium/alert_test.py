
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait								
from selenium.webdriver.support import expected_conditions as EC 

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.6play.fr")
time.sleep(2)
accept_btn=driver.find_elements(By.CLASS_NAME, "sc-1veuio6-0 cJKdVI sc-1esye45-1 lgIYbk")
import pdb; pdb.set_trace()
time.sleep(2)

aide_btn= driver.find_elements(By.CLASS_NAME, "sc-1esye45-0 cGpZDX").click()
time.sleep(3)

driver.quit()