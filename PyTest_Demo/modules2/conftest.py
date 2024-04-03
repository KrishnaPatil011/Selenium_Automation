import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture()  # decorator
def setup(browser):
     if browser== "chrome":
         from selenium.webdriver.chrome.service import Service
         ser_obj = Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
         driver = webdriver.Chrome(service=ser_obj)

     elif browser=="edge":
         from selenium.webdriver.edge.service import Service
         ser_obj=Service("C:\Python_Selenium\Drivers\edgedriver_win64\msedgedriver.exe")
         driver = webdriver.Edge(service=ser_obj)

     return driver


def pytest_addoption(parser):            #This will get value from CLI
        parser.addoption("--browser")

@pytest.fixture()
def browser(request):                     #This will return the browser value to setup method
    return request.config.getoption("--browser")

# Customizing HTML reort
# It is hook for adding the environmental info to html report

# def pytest_configure(config):
#     config._metadata['Project Name']='WebApp'
#     config._metadata['Module Name']='Login'
#     config._metadata['Tester Name'] = 'Krishna'

# # delete/modify the environment info of html report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("plugins",None)











