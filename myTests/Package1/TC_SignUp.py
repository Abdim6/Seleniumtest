import unittest

class SignupTest(unittest.TestCase):
    def test_signyEmail(self):
        self.assertTrue(True)
        print("This is sign by email test")
    
    def test_signbyFacebook(self):
        self.assertTrue(True)
        print("This is sign by Facebook test")
    
    def test_signbyGoogle(self):
        self.assertTrue(True)
        print("This is sign by Google test")

if __name__=="__main__":
    unittest.main()