#Test Case
#------------------
# 1) Open Web Browser(Chrome/firefox/Edge).
# 2) Open URL  https://admin.dev-k8.livingthings.co.in/
# 3) Enter username  (Admin).
# 4) Enter password  (aircon).
# 5) Click on Login.
# 6) Capture title of the home page.(Actual title)
# 7) Verify title of the page: Living Things Admin Portal (Expected)
# 8) close browser
import time
from selenium import webdriver
driver=webdriver.Chrome("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://admin.dev-k8.livingthings.co.in/")
driver.find_element_by_xpath("//input[@id='mat-input-0']").send_keys("admin")
driver.find_element_by_xpath("//input[@id='mat-input-1']").send_keys("aircon")
driver.find_element_by_xpath("//span[text()='Success']").click()


act_title=driver.title
exp_title="Living Things Admin Portal"

if act_title==exp_title:
    print("Login Test Passed")

else:
    print("Login Test Fail")

driver.close()





