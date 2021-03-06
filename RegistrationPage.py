import unittest
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.auto_locators import SignInLocators as SIL
from locators.auto_locators import MainPageLocators as MPL
from selenium.webdriver.common.by import By


class CreateAccount(unittest.TestCase):
    """Test of a creating an account"""

    def setUp(self):
        """Go into Sign In website"""
        self.driver = Firefox(executable_path=GeckoDriverManager().install())
        self.driver.get(
            'http://automationpractice.com/index.php?')

    def tearDown(self):
        self.driver.close()

    def test_creat_account(self):
        """Input data & create account."""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MPL.SIGN_IN)).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(SIL.EMAIL))


if __name__ == '__main__':
    unittest.main()
