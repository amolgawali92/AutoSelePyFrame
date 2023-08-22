#test_Login.py

import pytest

class TestLogin:
    def test_LoginByEmail(self,setup):
        print("Login using Email...")
        assert True == True
    def test_LoginByFacebook(self,setup):
        print("Login by Facebbok")
        assert True == True

    def test_LoginByTwitter(self,setup):
        print("Login By Twitter")
        assert True == True

