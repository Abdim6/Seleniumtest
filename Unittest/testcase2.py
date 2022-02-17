import unittest
from selenium import webdriver

class testSite(unittest.TestCase):
    def test_google(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.google.com/")
        print("Title of the page is :"+self.driver.title)
        print("-----------")
        # self.driver.close()
    def test_yahoo(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://fr.yahoo.com/")
        print("Title of the page is :"+self.driver.title)
        print("-----------")
        # self.driver.close()

if __name__ == "__main__":
    unittest.main()




    "fais toi une liste de tous les points de contrôle possible"
    "un apperçu du xml"
