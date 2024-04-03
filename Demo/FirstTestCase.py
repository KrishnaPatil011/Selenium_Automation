#Test Case
#------------------
# 1) Open Web Browser(Chrome/firefox/Edge).
# 2) Open URL  https://support.dev-k8.livingthings.co.in/login
# 3) Enter username  (Admin@gmail.com).
# 4) Enter password  (admin@123).
# 5) Click on Login.
# 6) Capture title of the home page.(Actual title)
# 7) Verify title of the page: OrangeHRM    (Expected)
# 8) close browser

from selenium import webdriver

driver=webdriver.Chrome("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")

# driver.get("https://www.facebook.com/")
# driver.maximize_window()
# driver.find_element_by_id("email").send_keys("admin@gmail.com")
# driver.find_element_by_id("pass").send_keys("admin@123")
# driver.find_element_by_name("login").click()

driver.get("https://support.dev-k8.livingthings.co.in/login")
driver.maximize_window()
# driver.findElement(By.xpath("//input[@type='email']")).sendKeys("admin@gmail.com")
driver.find_element_by_id("email").send_keys("admin@gmail.com")
driver.find_element_by_id("password").send_keys("admin@123")
driver.fullscreen_window()
# driver.find_element_by_class_name("btn btn-primary btn-login text-uppercase fw-bold").click()
# driver.find_element_by_xpath("//button[@type='submit']").click()
# driver.execute_script("window.scrollBy(0,650),")
login_button=driver.find_element_by_xpath("//button[@type='submit']")
# driver.execute_script("arguments[0].scrollIntoView();", login_button)

login_button.click()