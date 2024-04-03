#Test Case
#------------------
# 1) Open Web Browser(Chrome/firefox/Edge).
# 2) Open URL
# 3) Enter username
# 4) Enter password
# 5) Click on Login.
# 6) Capture title of the home page.(Actual title)
# 7) Verify title of the page: Living Things Admin Portal (Expected)
# 8) close browser
import time

from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

ser_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj,options=ops)
driver.implicitly_wait(20)

driver.maximize_window()
driver.get("https://webapp.livingthings.in/#/login")
driver.find_element(By.XPATH,"//input[@name='ion-input-0']").send_keys("7738067226")
driver.find_element(By.XPATH,"//input[@name='ion-input-1']").send_keys("0")
# driver.find_element_by_tag_name("ion-button").click()
driver.find_element(By.TAG_NAME,"ion-button").click()
time.sleep(3)
checkbox=driver.find_element(By.XPATH,"//input[@id='declare']")
checkbox.click()
select_checkbox=checkbox.is_selected()
print("Check box is selcted:",select_checkbox)
Submit=driver.find_element(By.XPATH,"//ion-button[@class='md button button-solid ion-activatable ion-focusable hydrated'][2]")
# Submit=driver.find_element(By.TAG_NAME,"ion-button")
# ion-button
Submit.click()
Submit.click()

act=ActionChains(driver)
act.double_click(Submit).perform()

act_title=driver.title
exp_title="Living Things"

if act_title==exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

# driver.close()



