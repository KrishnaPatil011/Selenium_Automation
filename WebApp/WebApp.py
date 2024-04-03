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
Submit.click()
Submit.click()  #login

url=driver.current_url
print(url)
act_title=driver.title
exp_title="Living Things"

if act_title==exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")


# click on the Analytics Dashboard

driver.find_element(By.XPATH,"//span[text()='Analytics']").click()
time.sleep(3)
url2=driver.current_url
print(url2)
act_url=url2
exp_url="https://webapp.livingthings.in/#/analytics?m=7738067226"
if act_url==exp_url:
    print("Analytics Dashboard page is open")
else:
    print("Analytics Dashboard is not open")

# Back to the home page
driver.back()
time.sleep(3)
url4=driver.current_url
print(url4)
act_url=url4
exp_url="https://webapp.livingthings.in/#/home-screen"
if act_url==exp_url:
    print("Back to home page")
else:
    print("Home page not open")


# Click on the schedule

driver.find_element(By.XPATH,"//span[text()='Schedules']").click()
url3=driver.current_url
print(url3)

act_url=url3
exp_url="https://webapp.livingthings.in/#/schedule-list?notificationCount=0"

if act_url==exp_url:
    print("Schedule page is open")
else:
    print("Schedule page is not open")
time.sleep(5)

# click on the add button

addbutton = driver.execute_script("return document.querySelector('ion-fab-button').shadowRoot.querySelector('button')")
js = "arguments[0].click();"
driver.execute_script(js, addbutton)
time.sleep(5)
schedule=driver.execute_script("return document.querySelector('body > app-root > ion-app > ion-router-outlet > app-schedule-list > ion-content > ion-fab > ion-fab-list > ion-fab-button:nth-child(1)').shadowRoot.querySelector('button > span.button-inner')")
js = "arguments[0].click();"
driver.execute_script(js, schedule)
driver.find_element(By.XPATH,"/html/body/app-root/ion-app/ion-router-outlet/app-add-schedule/ion-content/div/div[1]/div[1]/div/app-select-room[1]/ion-card/div/p").click()
time.sleep(3)
url5=driver.current_url
print(url5)
act_url=url5
exp_url="https://webapp.livingthings.in/#/add-schedule"
if act_url==exp_url:
    print("Add Schedule Page")
else:
    print("Add schedule page not open")


# back to schedule page
time.sleep(3)
driver.back()
url3=driver.current_url
print(url3)
act_url=url3
exp_url="https://webapp.livingthings.in/#/schedule-list?notificationCount=0"
if act_url==exp_url:
    print("Back to Schedule Page")
else:
    print("does not navigate to schedule page")
time.sleep(3)

# Back to the home page
driver.back()
# time.sleep(3)
url4=driver.current_url
print(url4)
act_url=url4
exp_url="https://webapp.livingthings.in/#/home-screen"
if act_url==exp_url:
    print("Back to home page")
else:
    print("Home page not open")

# Click on the Notification
driver.find_element(By.XPATH,"//span[text()='Notifications']").click()
url6=driver.current_url
print(url6)
act_url=url6
exp_url="https://webapp.livingthings.in/#/notification-list"
if act_url==exp_url:
    print("Notification page is open")
else:
    print("does not open the Notification page")

# Back to the home page
time.sleep(3)
driver.back()
url4=driver.current_url
print(url4)
act_url=url4
exp_url="https://webapp.livingthings.in/#/home-screen"
if act_url==exp_url:
    print("Back to home page")
else:
    print("Home page not open")

# Click on the create group button
driver.find_element(By.XPATH,"//span[text()='Create Group']").click()
url6=driver.current_url
print(url6)
act_url=url6
exp_url="https://webapp.livingthings.in/#/add-room"
if act_url==exp_url:
    print("Create Group page is open")
else:
    print("Group page not open")


# Back to the home page
time.sleep(3)
driver.back()
url4=driver.current_url
print(url4)
act_url=url4
exp_url="https://webapp.livingthings.in/#/home-screen"
if act_url==exp_url:
    print("Back to home page")
else:
    print("Home page not open")

#   click on the AC Overview
driver.find_element(By.XPATH,"//span[text()='AC Overview']").click()
url7=driver.current_url
print(url7)
act_url=url7
exp_url="https://webapp.livingthings.in/#/home-master?notificationCount=0"
if act_url==exp_url:
    print("AC Overview page is open")
else:
    print("AC Overview not open")

# back to home page
time.sleep(3)
driver.back()
url4=driver.current_url
print(url4)
act_url=url4
exp_url="https://webapp.livingthings.in/#/home-screen"
if act_url==exp_url:
    print("Back to home page")
else:
    print("Home page not open")


#   click on the Setting
driver.find_element(By.XPATH,"//span[text()='Settings']").click()
url7=driver.current_url
print(url7)
act_url=url7
exp_url="https://webapp.livingthings.in/#/settings?test=test"
if act_url==exp_url:
    print("Settings page is open")
else:
    print("Settings not open")

# back to home page
time.sleep(3)
driver.back()
url4=driver.current_url
print(url4)
act_url=url4
exp_url="https://webapp.livingthings.in/#/home-screen"
if act_url==exp_url:
    print("Back to home page")
else:
    print("Home page not open")

# click on the Log Out
driver.find_element(By.XPATH,"//span[text()='Log Out']").click()
# Logout=driver.execute_script("return document.querySelector('#ion-overlay-27 > div > app-message-dialog > app-alert-dialog > div > ion-card > ion-card-content > ion-row:nth-child(2) > ion-grid > ion-row:nth-child(2) > ion-button:nth-child(2)")
# js = "arguments[0].click();"
# driver.execute_script(js, Logout)
logout_element = driver.find_element(By.CSS_SELECTOR, "#ion-overlay-27 div app-message-dialog app-alert-dialog div ion-card ion-card-content ion-row:nth-child(2) ion-grid ion-row:nth-child(2) ion-button:nth-child(2)")
driver.execute_script("arguments[0].click();", logout_element)

time.sleep(3)
url8=driver.current_url
print(url8)
act_url=url8
exp_url="https://webapp.livingthings.in/#/login"
if act_url==exp_url:
    print("Successfully logout")
else:
    print("Logout Error")

driver.close()

