import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Testclass:
    @pytest.mark.parametrize('user,pwd',[("7410162452","Ayush2511"),("74101624522","Ayush2511"),("7410162452","Ayush251")])
    def test_login(self,user,pwd):
        self.ser_obj = Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.ser_obj)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("https://ltconfigweb.beta.livingthings.in/login")
        self.driver.find_element(By.XPATH, "//input[@type='text'][1]").send_keys(user)
        self.driver.find_element(By.XPATH, "//input[@type='password'][1]").send_keys(pwd)
        self.driver.find_element(By.XPATH, "//button[@type='submit'][1]").click()


        try:
            time.sleep(10)
            # self.connect=self.driver.find_element(By.XPATH, "//*[@id='root']/section/section/div[2]/div/div/form/div[2]/button")
            # self.connect.click()
            # self.act_url=self.driver.current_url
            self.act_url = self.driver.current_url
            self.driver.close()
            assert self.act_url=="https://ltconfigweb.beta.livingthings.in/"
            # assert self.connect == True
        except:
            self.driver.close()
            assert False



        # self.driver.find_element(By.XPATH, "//input[@name='macID']").send_keys("C8:F0:9E:29:41:31")
        # time.sleep(5)
        # self.driver.find_element(By.XPATH, "//button[text()='Connect']").click()


        # self.driver.get("https://webapp.livingthings.in/#/login")
        # self.driver.find_element(By.XPATH, "//input[@name='ion-input-0']").send_keys(user)
        # self.driver.find_element(By.XPATH, "//input[@name='ion-input-1']").clear()
        # self.driver.find_element(By.XPATH, "//input[@name='ion-input-1']").send_keys(pwd)
        # self.driver.find_element(By.TAG_NAME, "ion-button").click()
        # time.sleep(2)
        # try:
        #     self.checkbox = self.driver.find_element(By.XPATH, "//input[@id='declare']")
        #     self.checkbox.click()
        #     self.select_checkbox = self.checkbox.is_selected()
        #     print("Check box is selcted:", self.select_checkbox)
        #     self.Submit = self.driver.find_element(By.XPATH,"//ion-button[@class='md button button-solid ion-activatable ion-focusable hydrated'][2]")
        #     self.Submit.click()
        #     self.Submit.click()
        #     self.home= self.driver.find_element(By.XPATH,"//span[text()='Home']").is_displayed()
        #     self.driver.close()
        #     assert self.select_checkbox==True
        #
        # except:
        #     self.driver.close()
        #     assert False




