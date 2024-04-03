import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class TestFirst:
    # def test_logo(self,setup):
    #     self.driver=setup
    #     self.driver.get("https://webapp.livingthings.in/#/login")
    #     self.logo=self.driver.find_element(By.XPATH,"/html/body/app-root/ion-app/ion-router-outlet/app-login/ion-content/div/img").is_displayed()
    #     try:
    #         self.driver.close()
    #         assert self.logo==True
    #     except:
    #         self.driver.close()
    #         assert False

    @pytest.mark.parametrize('user,pwd', [("7738067226", "0"), ("773806722622", "0")])
    def test_login(self,user,pwd,setup):
        self.driver=setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        # self.ser_obj = Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        # self.driver = webdriver.Chrome(service=self.ser_obj)
        self.driver.get("https://webapp.livingthings.in/#/login")
        self.driver.find_element(By.XPATH, "//input[@name='ion-input-0']").send_keys(user)
        self.driver.find_element(By.XPATH, "//input[@name='ion-input-1']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='ion-input-1']").send_keys(pwd)
        self.driver.find_element(By.TAG_NAME, "ion-button").click()
        time.sleep(2)
        try:
            self.checkbox = self.driver.find_element(By.XPATH, "//input[@id='declare']")
            self.checkbox.click()
            time.sleep(2)
            self.select_checkbox = self.checkbox.is_selected()
            time.sleep(2)
            print("Check box is selcted:", self.select_checkbox)
            self.Submit = self.driver.find_element(By.XPATH,
                                                   "//ion-button[@class='md button button-solid ion-activatable ion-focusable hydrated'][2]")
            self.Submit.click()
            self.Submit.click()
            self.home = self.driver.find_element(By.XPATH, "//span[text()='Home']").is_displayed()
            self.driver.close()
            assert self.select_checkbox == True

        except:
            self.driver.close()
            assert False


