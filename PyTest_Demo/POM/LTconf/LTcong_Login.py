from selenium import webdriver
from selenium.webdriver.common.by import By


class Lt_login:
    userid_xpath="//input[@type='text'][1]"
    password_xpath="//input[@type='password'][1]"
    loginbutton_xapth="//button[@type='submit'][1]"

    macid_xpath="//input[@name='macID']"
    selectdropdown_xpath="//button[@type='button']"
    dev_xpath="//span[text()='Dev']"
    preprod_xpath="//span[text()='Pre Production']"
    prod_xpath="//span[text()='Production']"
    connectbutton_xpath = "//button[text()='Connect']"


    def __init__(self,driver):
        self.driver=driver


    def Enteruserid(self,user):
        id=self.driver.find_element(By.XPATH,self.userid_xpath)
        id.send_keys(user)

    def Enterpassword(self,pwd):
        enter_pwd=self.driver.find_element(By.XPATH,self.password_xpath)
        enter_pwd.send_keys(pwd)

    def Clickonlogin(self):
       self.driver.find_element(By.XPATH,self.loginbutton_xapth).click()


    def Enter_macid(self,macid):
        mac=self.driver.find_element(By.XPATH,self.macid_xpath)
        mac.send_keys(macid)

    def Click_on_dropdown(self):
        self.driver.find_element(By.XPATH,self.selectdropdown_xpath).click()

    def select_environment(self):
        self.driver.find_element(By.XPATH,self.dev_xpath).click()


    def click_on_connect(self):
        self.driver.find_element(By.XPATH,self.connectbutton_xpath).click()












