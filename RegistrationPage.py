import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from locators.auto_locators import SignInLocators as SIL
from locators.auto_locators import MainPageLocators as MPL


class Create(unittest.TestCase):
    """Test of a creating an account"""

    def setUp(self):
        self.driver = webdriver.Chrome(
            'C:\Program Files (x86)\Chromedriver.exe')
        self.driver.get(
            'http://automationpractice.com/index.php?')

    def tearDown(self):
        self.driver.close()

    def test_creat_account(self):
        self.driver.find_element(*MPL.CONTACT_US).click()


if __name__ == '__main__':
    unittest.main()
