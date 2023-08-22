import pytest
# I WANT TO EXECUTE  SPECIFIC GROUP OF METHODS/TEST METHODS THEN WE HAVE TO PASS COMMAND USING TERMINAL-
#  Usings below command you can execute different way on  using Terminal
# 1)  pytest -v -s -m "sanity" pytest_Framework\test_Grouping.py (Execute only sanity tests that I have mentioned below)
# 2)  pytest -v -s -m "regression" pytest_Framework\test_Grouping.py (Execute only regression tests that i have mentioned below)
# 3)  pytest -v -s -m "regression and sanity" pytest_Framework\test_Grouping.py (Execute only sanity and regression both tests that i have mentioned below)
# 4)  pytest -v -s -m "not regression" pytest_Framework\test_Grouping.py (Execute only sanity tests that i have mentioned below not a regression)
# 6)  pytest -v -s -m "not sanity" pytest_Framework\test_Grouping.py (Execute only regression tests that i have mentioned below)

class TestClass:

    @pytest.mark.sanity    # Its is a user defined or Customized marker names(sanity, regression.etc.)
    def test_LoginByEmail(self):
        print("Login using Email....")
        assert 1==1

    @pytest.mark.sanity  #Add all this customized marker name(sanity, regression etc..in ".ini" file.
    def test_LoginByFacebook(self):
        print("Login Using Facebook....")
        assert 1==1

    @pytest.mark.regression

    def test_LoginByInstagram(self):
        print("Login Using Instagram....")
        assert 1==1
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_signupByMail(self):
        print("sign up by mail")
        assert 1==1
    @pytest.mark.regression

    def test_signupByFacebook(self):
        print("sign up by Facebook")
        assert 1==1
    @pytest.mark.sanity
    @pytest.mark.regression
    def tets_signupByTwitter(self):
        print("sign up By Twitter")
        assert 1==1
