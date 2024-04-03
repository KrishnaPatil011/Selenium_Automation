#Test Case
#------------------
# 1) Open Web Browser(Chrome/firefox/Edge).
# 2) Open URL  https://ltconfigweb.dev-k8.livingthings.co.in/login
# 3) Enter username  (Admin).
# 4) Enter password  (aircon).
# 5) Click on Login.
# 6) Capture title of the home page.(Actual title)
# 7) Verify title of the page: Living Things Admin Portal (Expected)
# 8) close browser
import time


from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://ltconfigweb.beta.livingthings.in/login")

driver.find_element(By.XPATH,"//input[@type='text'][1]").send_keys("7410162452")
driver.find_element(By.XPATH,"//input[@type='password'][1]").send_keys("Ayush2511")
driver.find_element(By.XPATH,"//button[@type='submit'][1]").click()

# act_title=driver.title
# exp_title="LT - Field Application"
#
# if act_title==exp_title:
#     print("Login Test Passed")
# else:
#     print("Login Test Failed")


driver.find_element(By.XPATH,"//input[@name='macID']").send_keys("C8:F0:9E:29:41:31")
time.sleep(5)
driver.find_element(By.XPATH,"//button[@type='button']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//span[text()='Dev']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//button[text()='Connect']").click()



