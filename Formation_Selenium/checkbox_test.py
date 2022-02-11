
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait								
from selenium.webdriver.support import expected_conditions as EC 

driver = webdriver.Chrome()
driver.maximize_window()
driver.maximize_window()
driver.get("https://www.elllo.org/english/1451/1470-MegTodd-CompareMedia.htm")
time.sleep(2)
quiz_btn = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div[2]/ul/li[2]/a").click()
value=quiz_btn.get_attribute('class')
print(value)
# wait = WebDriverWait(driver,10)
# check_answers=wait.until(EC.visibility_of_element_located((By.ID,"q__")))

# print("Le bouton est visible-OK")
# check_box=driver.find_element(By.ID,"answer_0_0")
# import pdb; pdb.set_trace()
# all_questions=driver.find_elements(By.CLASS_NAME,"question")

time.sleep(2)
driver.quit()