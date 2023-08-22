import pytest

class TestClass:
    @pytest.fixture()
    def setup(self):
         print("Launch the browser...")   # Executes ones before every test method
         yield
         print("Close the Browser...")    # Execute ones after every test method
    def testLogin(self,setup):
        print("This is login")

    def test_Search(self,setup):
        print("This is search")

    def test_Logout(seif,setup):
        print("This is logout")
