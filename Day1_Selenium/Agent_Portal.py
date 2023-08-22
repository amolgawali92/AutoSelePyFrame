import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

# Website Launch

driver.get("https://agent-portal.cubedots.com/")
print(driver.title)

# Maximize the Window
driver.maximize_window()

# Agent Login Page

driver.find_element(By.XPATH,"//input[@id='amplify-id-:r1:']").send_keys("mehvish@cubedots.com")
driver.find_element(By.XPATH,"//input[@id='amplify-id-:r4:']").send_keys("Mehvish@123")

# Click on Signin Button

driver.find_element(By.XPATH,"//button[normalize-space()='Sign in']").click()

# Wait of 5 Sec for next actions
time.sleep(5)

# Open Sales Page

driver.find_element(By.LINK_TEXT,"Sales").click()
time.sleep(5)

#driver.switch_to.frame("ant-card ant-card-bordered sales-commission-insights css-1lt8isc")

# Click on This Year Button

driver.find_element(By.XPATH,"//span[normalize-space()='This Year']").click()
time.sleep(5)

# Open Projects Tab

driver.find_element(By.XPATH,"//a[normalize-space()='Projects']").click()
time.sleep(5)


# Hover on User Profile
driver.find_element(By.XPATH,"//p[@class='user-role']").click()
time.sleep(5)

#  Click on View More Button

driver.find_element(By.XPATH,"//div[@class='slick-slide slick-active slick-current']//div[@class='ant-row ant-row-center css-1lt8isc']//div[1]//div[2]//div[1]//a[1]//button[1]//span[1]").click()
time.sleep(5)

# Click on Marketing Button
driver.find_element(By.XPATH,"//a//button[@type='button']").click()
time.sleep(5)

# Open Photos
driver.find_element(By.XPATH,"//b[normalize-space()='Photos']").click()
time.sleep(5)

# Click on Image
driver.find_element(By.CLASS_NAME,"ant-image-mask-info").click()

# Click  cross button to Close Image
driver.find_element(By.XPATH,"//li[@class='ant-image-preview-operations-operation ant-image-preview-operations-operation-close']").click()
time.sleep(5)

# Open Cuverse Page
driver.find_element(By.XPATH,"//a[normalize-space()='Cuverse']").click()
time.sleep(5)

# Open Activity Page
driver.find_element(By.XPATH,"//a[normalize-space()='Activities']").click()
time.sleep(5)

# Click On Create Appointment Button
driver.find_element(By.XPATH,"//span[normalize-space()='Create Appointment']").click()
driver.find_element(By.ID,"notes").send_keys("Hi")
time.sleep(5)

# Select Date Picker on Form

#driver.find_element(By.XPATH,"//input[@id='date']").click()
#driver.switch_to.frame(0)
#year="2021"
#month="May"
#date="21"
#driver.find_element(By.XPATH,"//table[@class='ant-picker-content']").click()
#time.sleep(5)

# Fill Location field in Create Appointment Form
driver.find_element(By.ID,"location").send_keys("Tema Istanbul 2")
time.sleep(5)

# Click on Submit Button on Create Appointment Form
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(5)

# Click on Close icon on Create Appointment  Form
driver.find_element(By.XPATH,"//button[@aria-label='Close']").click()
time.sleep(5)

# Click on Cubedots Logo (Open Home Page)
driver.find_element(By.XPATH,"//img[@src='/assets/images/logo.png']").click()
time.sleep(10)

driver.find_element(By.CLASS_NAME,"ant-card-body").click()

# Click on Terms & Conditions Page
#driver.find_element(By.XPATH,"//div[contains(text(),'Terms & Conditions')]").click()

# Open Settings Page
# driver.find_element(By.LINK_TEXT,"Settings").click()

#driver.find_element(By.XPATH,"//a[normalize-space()='Sales']").click()

time.sleep(10)
driver.close()