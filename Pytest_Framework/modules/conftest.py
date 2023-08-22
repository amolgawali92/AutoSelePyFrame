import pytest

@pytest.fixture()     #decorator
def setup():
    print("Launching Browser....")
    yield
    print("Close the Browser.....")





