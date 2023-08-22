# importing the modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

# web page url
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# find id of option
down=driver.find_element(By.ID,"RESULT_RadioButton-9")
drop = Select(down)

# select by visible text
drop.select_by_visible_text("Evening")
time.sleep(4)
driver.close()