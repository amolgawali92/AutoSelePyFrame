import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_Obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_Obj)
driver.get("https://d1vws52eatcklr.cloudfront.net/")

driver.maximize_window()

driver.find_element(By.CLASS_NAME,"ant-image-img marketing-suite-img").click()

time.sleep(5)
driver.quit()