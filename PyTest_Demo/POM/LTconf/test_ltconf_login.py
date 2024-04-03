import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from LTcong_Login import Lt_login

class TestLogin:
    @pytest.mark.parametrize('user,pwd', [("7410162452", "Ayush2511"),("74101624521", "Ayush2511")])
    def test_login(self,user,pwd):
        # self.driver = setup
        serv_obj = Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_obj)
        self.driver.get("https://ltconfigweb.beta.livingthings.in/login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        lp = Lt_login(self.driver)
        lp.Enteruserid(user)
        lp.Enterpassword(pwd)
        lp.Clickonlogin()
        time.sleep(10)
        try:

            self.act_url1 = self.driver.current_url
            lp.Enter_macid("C8:F0:9E:29:41:31")
            lp.Click_on_dropdown()
            lp.select_environment()
            lp.click_on_connect()
            time.sleep(5)
            self.act_url2 = self.driver.current_url
            self.driver.close()
            assert self.act_url1 == "https://ltconfigweb.beta.livingthings.in/"
            assert self.act_url2 == "https://ltconfigweb.beta.livingthings.in/device"
        except:
            self.driver.close()
            assert False

        # self.act_title = self.driver.title
        # self.driver.close()
        # assert self.act_title == "LT - Field Application"
