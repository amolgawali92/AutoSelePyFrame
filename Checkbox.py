import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

Serv_Obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=Serv_Obj)

driver.get("https://d2swaiuslqgjgf.cloudfront.net/")
driver.maximize_window()

time.sleep(5)

driver.find_element(By.XPATH,"//div[@class='becomeOurPartnerBtnSection']//button").click()
driver.find_element(By.NAME,"firstName").send_keys("Test")

driver.find_element(By.NAME,"lastName").send_keys("T")
time.sleep(5)

driver.find_element(By.XPATH,"//input[@placeholder='Email Address *']").send_keys("test@gmail.com")

dropdown=driver.find_element(By.CLASS_NAME,"form-select")
drp = Select(dropdown)

drp.select_by_visible_text("Others")

time.sleep(5)
down=driver.find_element(By.NAME,"country")
down = Select(down)

down.select_by_visible_text("India")
time.sleep(5)

driver.find_element(By.NAME,"mobile").send_keys("12345698746")

driver.find_element(By.NAME,"message").send_keys("Test Mail....")

driver.find_element(By.ID,"flexCheckDefault").click()

#driver.find_element(By.NAME,"securityCode").send_keys("D88woq")
driver.find_element(By.CLASS_NAME,"btntheme").click()

time.sleep(5)
driver.close()