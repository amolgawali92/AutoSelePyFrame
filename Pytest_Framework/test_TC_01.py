import pytest

class TestClass:
    @pytest.fixture()      #decorator
    def setup(self):
        print("Launch the Browser")
        print("Open the Application")

    def test_Login(self,setup):
        print("This is Login Test")

    def test_Search(self,setup):
        print("This is Search")

    def test_Logout(self,setup):
        print("This is Logout")





