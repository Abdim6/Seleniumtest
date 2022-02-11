import unittest
from Package1.TC_Login import LoginTest
from Package1.TC_SignUp import SignupTest

"lancer des cas de test"
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)

lancertests = unittest.TestSuite([tc1,tc2])
unittest.TextTestRunner().run(lancertests)

