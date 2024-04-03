import time
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
# driver=webdriver.Chrome()
driver.get("https://support.dev-k8.livingthings.co.in/login")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.ID,"email").send_keys("admin@gmail.com")
