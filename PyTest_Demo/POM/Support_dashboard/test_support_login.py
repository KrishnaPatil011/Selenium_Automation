from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Support_login import LoginPage

class TestLogin:
    def test_login(self):
        serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        self.driver=webdriver.Chrome(service=serv_obj)
        self.driver.get("https://ops.livingthings.in/login")
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName("admin@gmail.com")
        self.lp.setPassword("icapo@0512")
        self.lp.Clicksignin()


        self.act_title=self.driver.title
        self.driver.close()
        assert self.act_title=="Living Things"

