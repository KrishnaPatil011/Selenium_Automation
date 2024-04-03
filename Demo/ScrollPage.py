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
driver.get("https://livingthings.in/")

# Scroll down Page by pixel
# driver.execute_script("window.scrollBy(0,1000)","")   #scroll by pixel
# value=driver.execute_script("return window.pageYOffset;")
# print(value) #1000

#2. Scroll down page till the element is visible
# tagline=driver.find_element(By.XPATH,"//*[@id='root']/div[5]/div/h1")
# driver.execute_script("arguments[0].scrollIntoView();",tagline)
# value=driver.execute_script("return window.pageYOffset;")
# print(value)

# 3.scroll down page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print(value)

time.sleep(5)
#4.Scroll up to starting position
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print(value)