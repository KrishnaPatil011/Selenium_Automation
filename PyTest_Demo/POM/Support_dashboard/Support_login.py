import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
 # locators
    username_xpath="//input[@type='email']"
    password_xpath="//input[@id='password']"
    signin_button_xpath="//button[@type='submit']"


# constructor
    def __init__(self,driver):
        self.driver=driver

# actions
    def setUserName(self,username):
        usernametxt=self.driver.find_element(By.XPATH,self.username_xpath)
        usernametxt.clear()
        usernametxt.send_keys(username)

    def setPassword(self,pwd):
        passwordtxt=self.driver.find_element(By.XPATH,self.password_xpath)
        passwordtxt.clear()
        passwordtxt.send_keys(pwd)

    def Clicksignin(self):
        scroll = self.driver.find_element_by_xpath("//div[@class='card-body p-3 p-sm-4']")
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll)
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.signin_button_xpath).click()
