import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.implicitly_wait(20)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']").click()
time.sleep(5)
alert=driver.switch_to.alert
alert.send_keys("welcome")
alert.text
# alert.accept()
alert.dismiss()
# driver.close()

