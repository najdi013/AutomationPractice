import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.auto_locators import ContactUsPageLocators as CPL


class ContactUs(unittest.TestCase):
    """First test of a contact form"""

    def setUp(self):
        self.driver = webdriver.Chrome(
            'C:\Program Files (x86)\Chromedriver.exe')
        self.driver.get(
            'http://automationpractice.com/index.php?')

    # def test_contact_form(self):
        """Tests automationpractice.com contact form. Make sure that you can click it, 
        chose subject, input email and order, attach file and write message. 
        Next you can send it"""

    def test_form_is_present(self):
        WebDriverWait(self, 10).until(
            EC.presence_of_element_located(*CPL.FORM)).click()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
