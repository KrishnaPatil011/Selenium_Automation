from selenium.webdriver.common.by import By


class Loginpage1:
    # Locators
    mobile_number_xpath="//input[@name='ion-input-0']"
    password_xpath="//input[@name='ion-input-1']"
    login_button_tagname="ion-button"
    checkbox_xpath="//input[@id='declare']"
    nextbutton_xpath="//ion-button[@class='md button button-solid ion-activatable ion-focusable hydrated'][2]"

    # constructor
    def __init__(self,driver):
        self.driver=driver


     #actions
    def setMobileNumber(self,mobilenumber):
        mobile=self.driver.find_element(By.XPATH,self.mobile_number_xpath)
        mobile.send_keys(mobilenumber)

    def setPassword(self,password):
       enterpass= self.driver.find_element(By.XPATH,self.password_xpath)
       enterpass.send_keys(password)

    def clickonlogin(self):
        loginbutton=self.driver.find_element(By.TAG_NAME,self.login_button_tagname)
        loginbutton.click()


    def selectcheckbox(self):
        self.driver.find_element(By.XPATH,self.checkbox_xpath).click()

    def nextbutton(self):
        next=self.driver.find_element(By.XPATH,self.nextbutton_xpath)
        next.click()
        next.click()













