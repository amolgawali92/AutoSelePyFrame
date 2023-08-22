import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
class TestClass:
    @pytest.mark.parametrize('user,pwd' ,[("admin","admin@123"),("Admi","admin123"),("Admin","admin123"),("admin","admin@12")])
    def test_Login(self,user,pwd):
        self.serv_obj=Service("C:\Drivers\chromedriver.exe")
        self.driver=webdriver.Chrome(service=self.serv_obj)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.NAME,"Username").send_keys(user)
        self.driver.find_element(By.NAME,"password").send_keys(pwd)
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
        try:
            self.status=self.driver.find_element(By.XPATH,"//h6[normalize-space()='Dashboard']").is_displayed()
            self.driver.close()
            assert self.status == True
        except:
            self.driver.close()
            assert False

