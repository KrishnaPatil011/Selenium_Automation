from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://chercher.tech/practice/practice-dropdowns-selenium-webdriver")
driver.maximize_window()

# driver.find_element(By.XPATH,"//select[@id='first']")
dropdown=Select(driver.find_element(By.XPATH,"//select[@id='first']"))
# select option from dropdown.
# dropdown.select_by_visible_text("Iphone")  #text
# dropdown.select_by_value("Apple")         #value="Apple"
# dropdown.select_by_index(2)          #index

# capture all the options and print them
alloptions=dropdown.options
print('total no.of options',len(alloptions))

# for opt in alloptions:
#     print(opt.text)     #print all dropdown text


# select option from dropdown without build-in method (select method)
for opt in alloptions:
    if opt.text=="Iphone":
        opt.click()
        break

# Print all option without select method
# Alloptions=driver.find_elements(By.XPATH,"//select[@id='first']/option")
# print(len(Alloptions))

