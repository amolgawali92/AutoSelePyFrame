import pytest

@pytest.fixture()
def setup():
    print("Once before every method1")

    def testmethod1(setup):
        print("This is test method1")
    def testmethod2():
        print("ThIS TEST METHOD2")

