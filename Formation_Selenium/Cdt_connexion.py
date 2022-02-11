
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("http://demostore.supersqa.com/my-account/")

username_btn = driver.find_element(By.ID, "username")
username_btn.send_keys("abdemdsd")
time.sleep(2)

pwd_btn = driver.find_element(By.ID, "password")
pwd_btn.send_keys("abdemdsd")
time.sleep(2)

validate_btn = driver.find_element(By.XPATH,'//*[@id="customer_login"]/div[1]/form/p[3]/button').click()
time.sleep(2)

error_msg = driver.find_element(By.CSS_SELECTOR, "#content > div > div.woocommerce > ul > li")
# message_error = error_msg.text()
# assert message_error=="Invalid username. ", "ERROR : le message d'erreur affiché n'est pas celui attendu"
print(error_msg.text)
print("PASS")

driver.quit()
