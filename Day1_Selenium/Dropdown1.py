import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_Obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_Obj)

driver.get("https://cubedots.com/projects/alya-konutlar%C4%B1")

driver.maximize_window()
time.sleep(5)

down=driver.find_element(By.NAME,"country")
drop = Select(down)

drop.select_by_visible_text("India")
time.sleep(5)
driver.quit()
