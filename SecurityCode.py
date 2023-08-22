import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://d2swaiuslqgjgf.cloudfront.net/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.XPATH,"//span[normalize-space()='Become Our Partner']").click()

all1=driver.find_element(By.ID,"notcp")
all2=driver.find_element(By.NAME,"securityCode")

act=ActionChains(driver)

#all1----Ctrl+A    Select the text
act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()

time.sleep(5)
#OR
#act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()  #single line command

#all1----CTRL+C  COPY TEXT
act.key_down(Keys.CONTROL)
act.send_keys("c")
act.key_up(Keys.CONTROL)
act.perform()

time.sleep(5)

#Press Tab Key TO Navigate to all2(second box tab)

act.send_keys(Keys.TAB).perform()

time.sleep(3)
#all2---- CTRL+V    Paste the copied Text

act.key_down(Keys.CONTROL)
act.send_keys("v")
act.key_up(Keys.CONTROL)
act.perform()

time.sleep(5)
#OR

#act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()



driver.close()
