import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLogin:
    def testLogin_chrome(self):
        from selenium.webdriver.chrome.service import Service
        self.serv_obj = Service("C:\Drivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.serv_obj)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.NAME,"username").send_keys("Admin")
        self.driver.find_element(By.NAME,"password").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
        self.driver.find_element(By.XPATH,"//img[@alt='client brand banner']").click()
        assert self.driver.title == "OrangeHRM Logo"
        self.driver.quit()

    def testLogin_edge(self):
        from selenium.webdriver.edge.service import Service
        self.serv_obj = Service("C:\Users\Adminit\PycharmProjects\Drivers\msedgedriver.exe")
        self.driver = webdriver.edge(service=self.serv_obj)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        self.driver.find_element(By.XPATH, "//img[@alt='client brand banner']").click()
        assert self.driver.title == "OrangeHRM Logo"
        self.driver.quit()


    def testLogin_firefox(self):
        from selenium.webdriver.firefox.service import Service
        self.serv_obj = Service("C:\Users\Adminit\PycharmProjects\Drivers\geckodriver.exe")
        self.driver = webdriver.firefox(service=self.serv_obj)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        self.driver.find_element(By.XPATH, "//img[@alt='client brand banner']").click()
        assert self.driver.title == "OrangeHRM Logo"
        self.driver.quit()