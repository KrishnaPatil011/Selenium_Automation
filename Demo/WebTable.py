# 1) Count number of rows & columns
# 2) Read specific row & Column data
# 3) Read all the rows & Columns data
# 4) Read data based on condition(List books name whose author is Mukesh)

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")


# 1) Count number of rows & columns

noofRows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
noofcol=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr/th"))
print(noofRows)
print(noofcol)

# # 2) Read specific row & Column data  - Master In Selenium
# data=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[5]/td[1]").text
# print(data)

# 3) Read all the rows & Columns data

print("printing all the rows and columns data.....................")

# for r in range(2,noofRows+1):
#     for c in range(1,noofcol+1):
#         data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#         print(data,end='                 ')
#     print()


# 4) Read data based on condition(List books name whose author is Mukesh)
for r in range(2,noofRows+1):
    authorName=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if authorName=="Mukesh":
        bookName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[1]").text
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]").text
        print(bookName,"         ",authorName,"       ",price)


driver.close()
