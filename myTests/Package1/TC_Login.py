import unittest

class LoginTest(unittest.TestCase):
    def test_loginbyEmail(self):
        print("This is login by email test")
        self.assertTrue(True)
    
    def test_loginbyFacebook(self):
        print("This is login by Facebook test")
        self.assertTrue(True)
    
    def test_loginbyGoogle(self):
        print("This is login by Google test")
        self.assertTrue(True)

if __name__=="__main__":
    unittest.main()