import unittest
from selenium import webdriver
import page


class ContactUs(unittest.TestCase):
    """First test of a contact form"""

    def setUp(self):
        self.driver = webdriver
        self.driver.get('http://automationpractice.com/index.php')

    def test_contact_form(self):
        """Tests automationpractice.com contact form. Make sure that you can click it, 
        chose subject, input email and order, attach file and write message. 
        Next you can send it"""

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
