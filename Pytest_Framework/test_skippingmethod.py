import pytest

class TestClass:
    def test_LoginbyEmail(self):
        print("Login by Email")
        assert True == True

    @pytest.mark.skip   # used for skipped the test method
    def test_Loginbyinstagram(self):
        print("Login using instagram")
        assert True == True

    def test_payment_gpay(self):
        print("Pay using Gpay")
        assert 1 == 1
    @pytest.mark.skip
    def test_payment_Phonepay(self):
        print("Pay using Phonepe")
        assert 1==1

