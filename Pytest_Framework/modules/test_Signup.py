#test_Signup.py

import pytest

class TestSignup:
    def test_SignupByEmail(self,setup):
        print("Signup by email")
        assert True == True

    def test_SignupByFacebook(self,setup):
        print("Signup using Facebook")
        True == True
    def test_SignupByInstagram(self):
        print("Signup using instagram")
        assert True == True

