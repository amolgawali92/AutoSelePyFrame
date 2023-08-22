import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_Object=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_Object)

driver.get("https://agent-portal.cubedots.com/")

# Print Title of the Page
print(driver.title)

# Maximize the Window
driver.maximize_window()

# Agent Login Page

driver.find_element(By.XPATH,"//input[@id='amplify-id-:r1:']").send_keys("mehvish@cubedots.com")
driver.find_element(By.XPATH,"//input[@id='amplify-id-:r4:']").send_keys("Mehvish@123")
time.sleep(5)

# Click on Signin Button
driver.find_element(By.XPATH,"//button[normalize-space()='Sign in']").click()
time.sleep(5)

# Open Projects Page
driver.find_element(By.XPATH,"//a[normalize-space()='Projects']").click()
time.sleep(5)

# Click on 2nd page
driver.find_element(By.XPATH,"//a[normalize-space()='Next']").click()
time.sleep(5)

driver.close()
