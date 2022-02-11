
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Seconnecter:
    invalid_email = "abdfrabd@gmail.fr"

    def __init__(self) :
        self.driver = webdriver.Chrome()
        self.driver.get("http://demostore.supersqa.com/")
        self.driver.maximize_window()
        self.driver.maximize_window()
        myaccount_btn = self.driver.find_element(By.XPATH, '//*[@id="site-navigation"]/div[1]/ul/li[4]/a').click()
        time.sleep(2)

    def saisir_email(self):
        id_section = self.driver.find_element(By.ID,"reg_email")
        id_section.clear()
        # id_section.send_keys("my_email")
        id_section.send_keys(self.invalid_email)
        time.sleep(3)
        
    def saisir_pwd(self):
        pwd_section = self.driver.find_element(By.ID, "reg_password")
        pwd_section.send_keys("aze5")
        time.sleep(3)
        
    def clicker_btn(self):
        import pdb; pdb.set_trace()
        Submit_btn = self.driver.find_element(By.XPATH, '//*[@id="customer_login"]/div[2]/form/p[3]/button').click()

    def main(self):
        self.saisir_email()
        self.saisir_pwd()
        self.clicker_btn()
        print("PASS")
        time.sleep(2)
        # self.driver.quit()       


if __name__ == '__main__':
    obj = Seconnecter()
    obj.main()
