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

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")


ser_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.implicitly_wait(20)
driver.maximize_window()
driver.get("https://mbl.dev-k8.livingthings.co.in/")
driver.find_element(By.XPATH,"//input[@name='ion-input-0']").send_keys("7738067226")
driver.find_element(By.XPATH,"//input[@name='ion-input-1']").clear()
driver.find_element(By.XPATH,"//input[@name='ion-input-1']").send_keys("0")
driver.find_element(By.TAG_NAME,"ion-button").click()
time.sleep(5)
checkbox=driver.find_element(By.XPATH,"//input[@id='declare']")
checkbox.click()
select_checkbox=checkbox.is_selected()
print("Check box is selcted:",select_checkbox)
Submit=driver.find_element(By.XPATH,"//ion-button[@class='md button button-solid ion-activatable ion-focusable hydrated'][2]")
Submit.click()
Submit.click()

act_title=driver.title
exp_title="Living Things"

if act_title==exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")


# Click on the schedule
driver.find_element(By.XPATH,"//span[text()='Schedules']").click()


time.sleep(5)
addbutton = driver.execute_script("return document.querySelector('ion-fab-button').shadowRoot.querySelector('button')")
js = "arguments[0].click();"
driver.execute_script(js, addbutton)
time.sleep(5)
schedule=driver.execute_script("return document.querySelector('body > app-root > ion-app > ion-router-outlet > app-schedule-list > ion-content > ion-fab > ion-fab-list > ion-fab-button:nth-child(1)').shadowRoot.querySelector('button > span.button-inner')")
js = "arguments[0].click();"
driver.execute_script(js, schedule)

driver.find_element(By.XPATH,"/html/body/app-root/ion-app/ion-router-outlet/app-add-schedule/ion-content/div/div[1]/div[1]/div/app-select-room[1]/ion-card/div/p").click()
ime.sleep(5)
driver.find_element(By.XPATH,"/html/body/app-root/ion-app/ion-router-outlet/app-add-schedule/ion-content/div/div[1]/div[2]/div/div/app-select-switch/ion-card").click()






