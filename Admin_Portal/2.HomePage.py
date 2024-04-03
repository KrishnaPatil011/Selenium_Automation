import time
from selenium import webdriver
driver=webdriver.Chrome("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")

driver.maximize_window()
driver.get("https://admin.dev-k8.livingthings.co.in/")
time.sleep(3)
driver.find_element_by_xpath("//input[@id='mat-input-0']").send_keys("admin")
time.sleep(3)
driver.find_element_by_xpath("//input[@id='mat-input-1']").send_keys("aircon")
time.sleep(3)
driver.find_element_by_xpath("//span[text()='Success']").click()
time.sleep(3)


# Click on the client
driver.find_element_by_xpath("//p[text()='Clients']").click()
time.sleep(3)
# Click on the add client
driver.find_element_by_xpath("//button[text()='Add Client']").click()
time.sleep(3)

# Register Client
driver.find_element_by_xpath("//input[@id='mat-input-3']").send_keys("Livingthing_Office")
time.sleep(3)
driver.find_element_by_xpath("//input[@id='mat-input-4']").send_keys("livingthing@gmail.com")
time.sleep(3)
driver.find_element_by_xpath("//input[@id='mat-input-5']").send_keys("9730637199")
time.sleep(3)
driver.find_element_by_xpath("//input[@id='mat-input-6']").send_keys("Powai")
time.sleep(3)
driver.find_element_by_xpath("//input[@id='mat-input-7']").send_keys("400078")
time.sleep(3)
driver.find_element_by_xpath("//input[@id='mat-input-8']").send_keys("Mumbai")
time.sleep(3)
driver.find_element_by_xpath("//input[@id='mat-input-9']").send_keys("Maharashtra")
time.sleep(3)
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(3)
driver.find_element_by_xpath("//span[text()='Cancel']").click()         #Click on the cancel button


# Srach Bar
time.sleep(3)
driver.find_element_by_xpath("//input[@id='mat-input-2']").send_keys("Livingthing_Office")
time.sleep(3)
driver.find_element_by_xpath("//button[text()='Delete']").click()




