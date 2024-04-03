import time

from selenium import webdriver

driver=webdriver.Chrome("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver.get("https://ops.livingthings.in/login")
driver.maximize_window()
time.sleep(3)
driver.find_element_by_id("email").send_keys("admin@gmail.com")
time.sleep(3)
driver.find_element_by_id("password").send_keys("admin@123")
time.sleep(3)
# driver.fullscreen_window()
time.sleep(3)
# driver.find_element_by_class_name("btn btn-primary btn-login text-uppercase fw-bold").click()
# driver.find_element_by_xpath("//button[@type='submit']").click()
# driver.execute_script("window.scrollBy(0,650),")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(3)
scroll=driver.find_element_by_xpath("//div[@class='card-body p-3 p-sm-4']")
time.sleep(3)
driver.execute_script("arguments[0].scrollIntoView();", scroll)
time.sleep(3)
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(5)
act_title=driver.title
exp_title="Living Things"

if act_title==exp_title:
    print("Login Test Pass")
else:
    print("Login Test Fail")

driver.close()




