from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """Main page locators. All of them should go to this class."""

    CONTACT_US = (By.ID, 'contact-link')
    SIGN_IN = (By.CSS_SELECTOR, 'a.login')


class ContactUsPageLocators(object):
    """Contact page locators. All of them should go to this class."""

    FORM = (By.CSS_SELECTOR, 'form.contact-form-box')
    SUBJECT_HEADING = (By.ID, 'id_contact')
    EMAIL_ADDRESS = (By.ID, 'email')
    ORDER_REFERENCE = (By.ID, 'id_order')
    #CHOOSE_FILE = ()
    MESSAGE = (By.ID, 'message')
    SEND = (By.ID, 'submitMessage')


class SignInLocators(object):

    EMAIL = (By.ID, 'email_create')
    CREATE_ACCOUNT = (By.ID, 'SubmitCreate')
