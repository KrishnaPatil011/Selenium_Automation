import pytest

class TestClass:

    @pytest.fixture() #decorator
    def setup(self):
        print("launching browser")
        print("open application")

    def test_login(self,setup):
        print("This is login test")
    def test_search(self,setup):
        print("This is search test")

    def test_advanceseasrch(self,setup):
        print("this is advance search test")