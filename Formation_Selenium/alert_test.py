
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait								
from selenium.webdriver.support import expected_conditions as EC 

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.6play.fr")
time.sleep(3)

accepter_btn = driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(12) > aside > div > div.suptlw-3.dTtZno > form > div.s9pqpz-4.eGAKcX.sc-18bqyzn-0.gXHDvG > div > button.sc-1esye45-2.dVskuE.sc-1veuio6-0.dktssj.s9pqpz-2.hEklsz.is-primary > span")
accepter_btn.click()
time.sleep(3)

print(driver.get_log("driver"))
# "Scrooler vers le footer"
# footer_btn = driver.find_element(By.LINK_TEXT, "Tous les programmes")
# footer_btn.location_once_scrolled_into_view

# "capture d'écran"
# driver.get_screenshot_as_file("footer.png")

# aide_btn= driver.find_elements(By.CLASS_NAME, "sc-1esye45-0 cGpZDX").click()
time.sleep(3)

driver.quit()