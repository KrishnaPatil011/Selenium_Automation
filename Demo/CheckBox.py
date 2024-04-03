from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

# 1.Select specific checkbox

# driver.find_element(By.XPATH,"//input[@id='sunday']").click()

# 2.Select all the checkbox

checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes))
# Approach 1
# for i in range(len(checkboxes)):
#     checkbox[i].click()

# Approach 2
for checkbox in checkboxes:
    checkbox.click()

# 3. select multiple checkbox by choice
# for checkbox in checkboxes:
#     weekname=checkbox.get_attribute('id')
#     if weekname=='monday' or weekname=='sunday':
#           checkbox.click()

# 4.Select last 2 checkbox
# for i in range(len(checkboxes)-2,len(checkboxes)):      #range(5,7)
#     checkboxes[i].click()


# 5.select first 2 checkbox
# for i in range(len(checkboxes)):
#     if i<2:
#      checkboxes[i].click()

# 6.clearing all the check boxes
for checkbox in checkboxes:
 if checkbox.is_selected():
      checkbox.click()


