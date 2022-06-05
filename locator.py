from email.message import Message
from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """Main page locators. All of them should go to this class."""

    CONTACT_US = (By.ID, 'contact-link')


class ContactUsPageLocators(object):
    """Contact page locators. All of them should go to this class."""

    SUBJECT_HEADING = (By.ID, 'id_contact')
    EMAIL_ADDRESS = (By.ID, 'email')
    ORDER_REFERENCE = (By.ID, 'id_order')
    #CHOOSE_FILE = ()
    MESSAGE = (By.ID, 'message')
    SEND = (By.ID, 'submitMessage')
