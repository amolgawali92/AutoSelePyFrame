import pytest

class TestClass:

    @pytest.mark.dependency()
    def test_OpenApp(self):
        assert True

    @pytest.mark.dependency(depends=['TestClass::test_OpenApp'])
    def test_LoginApp(self):
        assert True

    @pytest.mark.dependency(depends=['TestClass::test_LoginApp'])
    def test_SearchApp(self):
        assert True

    @pytest.mark.dependency(depends=['TestClass::test_LoginApp','TestClass::test_SearchApp'])
    def test_advSearch(self):
        assert True


    @pytest.mark.dependency(depends=['TestClass::testLoginApp'])
    def test_Logout(self):
        assert True



