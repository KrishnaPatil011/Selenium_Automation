import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webapp_login import Loginpage1

class TestLogin:
    def test_login(self):
        serv_obj = Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_obj)
        self.driver.get("https://webapp.livingthings.in/#/login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        lp=Loginpage1(self.driver)
        lp.setMobileNumber("7738067226")
        lp.setPassword("0")
        time.sleep(2)
        lp.clickonlogin()
        time.sleep(2)
        lp.selectcheckbox()
        time.sleep(2)
        lp.nextbutton()
        time.sleep(2)
        self.act_title = self.driver.title
        self.driver.close()
        assert self.act_title == "Living Things"


