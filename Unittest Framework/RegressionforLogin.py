import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class RegressionTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def tearDown(self):
        self.driver.quit()

class RegressionTest(unittest.TestCase):

    def test_valid_login(self):

        self.driver.get("https://staging-agent-portal.cubedots.com/")
        username = self.driver.find_element(By.XPATH, "//input[@id='amplify-id-:r1:']").send_keys("mehvish@cubedots.com")
        password = self.driver.find_element(By.XPATH, "//input[@id='amplify-id-:r4:']").send_keys("Mehvish@123")

        # Click on Signin Button

        click = self.driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']").click()

        self.assertTrue(self.driver.find_element(By.XPATH,"//button[@class='sign-out']"))

    def test_invalid_login(self):

        self.driver.get("https://staging-agent-portal.cubedots.com/")
        username = self.driver.find_element(By.XPATH,"//input[@id='amplify-id-:r1:']").send_keys("mehvis@cubedots.com")
        password = self.driver.find_element(By.XPATH,"//input[@id='amplify-id-:r4:']").send_keys("Mehvish@1")

        self.assertTrue(self.driver.find_element(By.XPATH,"//button[@class='sign-out']"))

        if __name__ == "__main__":
            unittest.main()


