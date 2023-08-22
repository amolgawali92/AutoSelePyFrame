import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

serv_Obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_Obj)

driver.get("https://demoqa.com/alerts")
#driver.implicitly_wait(5)
#W=WebDriverWait(driver, 10)
#W.until(expected_conditions.alert_is_present())
driver.maximize_window()
#time.sleep(5)
driver.find_element(By.ID,"alertButton").click()

alert=driver.switch_to.alert
print(alert)
alert.accept()
time.sleep(5)
driver.close()

