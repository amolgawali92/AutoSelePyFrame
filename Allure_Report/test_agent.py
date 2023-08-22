import self as self
from Tools.scripts.patchcheck import status
from selenium import webdriver
import allure
import pytest
from selenium.webdriver.common import by


# Allure reports in selenium with Python and Pytest

#Create one class and class name always start with Test
class TestHRM:
    def test_Logo(self):    # inside a class create test method "def" and test method start with the "test" keyword
      self.driver=webdriver.Chrome()
      self.driver.get("https://staging-agent-portal.cubedots.com/")
      status=self.driver.find_element_by_xpath("//img[@src='/assets/images/logo.png']").is_displayed()
      if status==True:
        assert True
      else:
        assert False
      self.driver.close()

    def test_listemp(self):

        pytest.skip('Skipped Test')

    def test_Login(self):

       self.driver = webdriver.Chrome()
       self.driver.get("https://staging-agent-portal.cubedots.com/")

       self.driver.find_element_by.xpath("//input[@id='amplify-id-:r1:']").send_keys("mehvish@cubedots.com")
       self.driver.find_element_by.xpath("//input[@id='amplify-id-:r4:']").send_keys("Mehvish@123")
       self.driver.find_element_by.xpath("//button[normalize-space()='Sign in']").click()
       act_title=self.driver.title

       if act_title=="Cubedots":
         self.driver.close()
         assert True
       else:
         self.driver.close()






