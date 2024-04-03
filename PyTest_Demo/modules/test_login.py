#test_login

import pytest

class Testlogin:
    def test_loginByEmail(self,setup):
        print("This is login by email..")
        assert True==True

    def test_loginByFacebook(self,setup):
        print("This is login by Fackebook..")
        assert True == True

    def test_loginByTwitter(self,setup):
        print("This is login by Twitter..")
        assert True == True

