from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service('C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver=webdriver.Chrome(service=serv_obj)
driver.get('https://demo.opencart.com/')
driver.maximize_window()
# Click on the link
# driver.find_element(By.LINK_TEXT,'MP3 Players').click()       #link text
# driver.find_element(By.PARTIAL_LINK_TEXT,'MP3').click()  #Partial link test

# Find total link on the page.
links=driver.find_elements(By.TAG_NAME,'a')
# total_link=driver.find_elements(By.XPATH,'//a')
print(len(links))

for link in links:
    print(link.text)

driver.close()