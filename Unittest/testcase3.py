import unittest
from selenium import webdriver


class AppTest(unittest.TestCase):

    @classmethod
    def setUp(self) :
        print("This is set up methode")
    @classmethod    
    def tearDown(self) :
        print("----This is the teardown----")
    @classmethod
    def setUpClass(cls):
        print("Ouverture de l'application")
    @classmethod
    def tearDownClass(cls):
        print("Fermeture de l'application")

    def test_search(self):
        print("This is search test")
    def test_advancedsearch(self):
        print("This is advanced search test")
    def test_prepaid(self):
        print("This is pre paid test")
    def test_postpaid(self):
        print("This is post paid test")


if __name__ == "__main__":
    unittest.main()