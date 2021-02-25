# -*- coding: UTF-8 -*-
import logging
import random
from StoreBase import StoreBase
from selenium.webdriver.common.by import By
import config
import string

# configuration
logger = logging.getLogger(__name__)
cfg = config.get_common_configs()

random_email = cfg['user_login_prefix'] + ''.join(random.sample(string.ascii_letters + string.digits, 15)) + \
               cfg['user_login_postfix']


class LoginFlowNavigationLocators:
    SIGN_IN_MAIN_MENU_BUTTON = (By.CLASS_NAME, "login")
    HOME_PAGE_TABS = (By.ID, "home-page-tabs")
    BLOCK_TOP_MENU = (By.ID, "block_top_menu")
    HEADER_LOGO = (By.CSS_SELECTOR, ".logo")
    PAGE_HEADER = (By.XPATH, "//*[contains(@class, 'page-heading')]")
    CREATE_ACCOUNT_EMAIL_INPUT = (By.ID, "email_create")
    LOGIN_EMAIL_INPUT = (By.ID, "email")
    LOGIN_PASSWORD_INPUT = (By.ID, "passwd")
    CREATE_ACCOUNT_BUTTON = (By.ID, "SubmitCreate")
    LOGIN_BUTTON = (By.ID, "SubmitLogin")
    CREATE_ACCOUNT_BOX = (By.ID, "create-account_form")
    LOGIN_ACCOUNT_BOX = (By.ID, "login_form")
    CREATE_EMAIL_VALID_ALERT = (By.XPATH, "//*[@id='create-account_form']//*[@class='form-group form-ok']")
    LOGIN_EMAIL_VALID_ALERT = (By.XPATH, "//*[@id='login_form']//*[@class='form-group form-ok']")
    ACCOUNT_CREATION_FORM = (By.ID, "account-creation_form")
    MALE_GENDER = (By.ID, "uniform-id_gender1")
    FEMALE_GENDER = (By.ID, "uniform-id_gender2")
    NAME_INPUT = (By.ID, "customer_firstname")
    LAST_NAME_INPUT = (By.ID, "customer_lastname")
    PASSWORD_INPUT = (By.ID, "passwd")
    EMAIL_INPUT = (By.ID, "email")
    DAY_OF_BIRTH = (By.ID, "days")
    MONTH_OF_BIRTH = (By.ID, "months")
    YEAR_OF_BIRTH = (By.ID, "years")
    ADDRESS_FIRST_NAME = (By.ID, "firstname")
    ADDRESS_LAST_NAME = (By.ID, "lastname")
    ADDRESS_LINE = (By.ID, "address1")
    CITY = (By.ID, "city")
    STATE = (By.ID, "id_state")
    ZIP = (By.ID, "postcode")
    COUNTRY = (By.ID, "id_country")
    PHONE = (By.ID, "phone")
    SUBMIT_BUTTON = (By.ID, "submitAccount")
    MY_ACCOUNT_MENU = (By.XPATH, "//*[contains(@class, 'row addresses-lists')]")
    MY_ACCOUNT_INFO = (By.XPATH, "//*[contains(@class, 'info-account')]")
    BREADCRUMB = (By.XPATH, "//*[contains(@class, 'navigation_page')]")
    CREATE_ACCOUNT_TITLE = (By.XPATH, "//*[contains(@id, 'create-account_form')]/*[contains(@class,"
                                      "'page-subheading')]")
    REGISTERED_ACCOUNT_TITLE = (By.XPATH, "//*[contains(@id, 'login_form')]/*[contains(@class,"
                                          "'page-subheading')]")
    CREATE_ACCOUNT_INFO = (
        By.XPATH, "//*[contains(@id, 'create-account_form')]/*[contains(@class, 'form_content clearfix')]//p")
    INVALID_DATA_CREATION_ALERT = (By.XPATH, "//*[@id='create_account_error']")
    INVALID_DATA_CREATION_ALERT_TEXT = (By.XPATH, "//*[@class='alert alert-danger']/ol/li")
    INVALID_DATA_LOGIN_ALERT = (By.XPATH, "//*[@class='alert alert-danger']")
    INVALID_DATA_LOGIN_ALERT_TEXT = (By.XPATH, "//*[@class='alert alert-danger']/ol/li")


class LoginFlowLexemes:
    CREATE_ACCOUNT_PAGE_HEADER = 'AUTHENTICATION'
    BREADCRUMB_NAVIGATION = 'Authentication'
    CREATE_ACCOUNT_TITLE = 'CREATE AN ACCOUNT'
    LOGIN_TITLE = 'ALREADY REGISTERED?'
    CREATE_ACCOUNT_INFO_TEXT = 'Please enter your email address to create an account.'
    INVALID_EMAIL_ADDRESS = 'Invalid email address.'
    USER_EXISTS = 'An account using this email address has already been registered. Please enter a valid password or ' \
                  'request a new one.'


class LoginFlowHelper(StoreBase):

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_the_main_logo(self):
        return self.click_element(LoginFlowNavigationLocators.HEADER_LOGO, time=2)

    def open_sign_in_page(self):
        self.go_to_main_page()
        self.find_element(LoginFlowNavigationLocators.HEADER_LOGO)
        logger.info('main page %s is loaded' % self.base_url)
        self.click_element(LoginFlowNavigationLocators.SIGN_IN_MAIN_MENU_BUTTON, time=2)
        self.wait_for_page_load(LoginFlowNavigationLocators.HOME_PAGE_TABS)
        logger.info('sign_in page %s is loaded' % self.get_current_url())
        self.find_element(LoginFlowNavigationLocators.CREATE_ACCOUNT_BOX, time=2)
        self.find_element(LoginFlowNavigationLocators.LOGIN_ACCOUNT_BOX, time=2)

    def verify_lexemes_sign_in_page(self):
        assert LoginFlowLexemes.CREATE_ACCOUNT_PAGE_HEADER == self.find_element(
            LoginFlowNavigationLocators.PAGE_HEADER).text
        assert LoginFlowLexemes.BREADCRUMB_NAVIGATION == self.find_element(LoginFlowNavigationLocators.BREADCRUMB).text
        assert LoginFlowLexemes.CREATE_ACCOUNT_TITLE == self.find_element(
            LoginFlowNavigationLocators.CREATE_ACCOUNT_TITLE).text
        assert LoginFlowLexemes.LOGIN_TITLE == self.find_element(
            LoginFlowNavigationLocators.REGISTERED_ACCOUNT_TITLE).text
        assert LoginFlowLexemes.CREATE_ACCOUNT_INFO_TEXT == self.find_element(
            LoginFlowNavigationLocators.CREATE_ACCOUNT_INFO).text

    def fill_in_email_to_create_account(self):
        self.input_data(LoginFlowNavigationLocators.CREATE_ACCOUNT_EMAIL_INPUT, random_email)

    def submit_button_to_create_account(self):
        self.click_element(LoginFlowNavigationLocators.CREATE_ACCOUNT_BUTTON)

    def fill_in_email_to_log_in(self):
        self.input_data(LoginFlowNavigationLocators.LOGIN_EMAIL_INPUT, cfg['user_email'])

    def fill_in_password_to_log_in(self):
        self.input_data(LoginFlowNavigationLocators.LOGIN_PASSWORD_INPUT, cfg['password'])
        self.find_element(LoginFlowNavigationLocators.LOGIN_EMAIL_VALID_ALERT)

    def submit_button_to_login(self):
        self.click_element(LoginFlowNavigationLocators.LOGIN_BUTTON)

    def fill_in_exist_email_to_create_account(self):
        self.input_data(LoginFlowNavigationLocators.CREATE_ACCOUNT_EMAIL_INPUT, cfg['user_email'])

    def fill_in_invalid_date_to_login(self):
        self.input_data(LoginFlowNavigationLocators.LOGIN_EMAIL_INPUT, cfg['invalid_email'])
        self.input_data(LoginFlowNavigationLocators.PASSWORD_INPUT, 'qwe')

    def verify_invalid_data_alert_for_create_acc_form(self):
        self.find_element(LoginFlowNavigationLocators.INVALID_DATA_CREATION_ALERT)
        assert self.find_element(
                LoginFlowNavigationLocators.INVALID_DATA_CREATION_ALERT_TEXT).text == LoginFlowLexemes.USER_EXISTS

    def verify_invalid_data_alert_for_login_form(self):
        self.find_element(LoginFlowNavigationLocators.INVALID_DATA_LOGIN_ALERT)
        assert self.find_element(
                LoginFlowNavigationLocators.INVALID_DATA_LOGIN_ALERT_TEXT).text == LoginFlowLexemes.INVALID_EMAIL_ADDRESS

    def fill_in_registration_form(self):
        self.click_element(LoginFlowNavigationLocators.MALE_GENDER, time=2)
        self.input_data(LoginFlowNavigationLocators.NAME_INPUT, cfg['name'])
        self.input_data(LoginFlowNavigationLocators.LAST_NAME_INPUT, cfg['last_name'])
        assert self.get_attr(LoginFlowNavigationLocators.EMAIL_INPUT, "value") is not None
        self.input_data(LoginFlowNavigationLocators.PASSWORD_INPUT, cfg['password'])
        self.select_element(LoginFlowNavigationLocators.DAY_OF_BIRTH, 'by_value', cfg['day_of_birth'])
        self.select_element(LoginFlowNavigationLocators.MONTH_OF_BIRTH, 'by_value', cfg['month_of_birth'])
        self.select_element(LoginFlowNavigationLocators.YEAR_OF_BIRTH, 'by_value', cfg['year_of_birth'])
        self.input_data(LoginFlowNavigationLocators.ADDRESS_FIRST_NAME, cfg['name'])
        self.input_data(LoginFlowNavigationLocators.ADDRESS_LAST_NAME, cfg['last_name'])
        self.input_data(LoginFlowNavigationLocators.ADDRESS_LINE, cfg['address'])
        self.input_data(LoginFlowNavigationLocators.CITY, cfg['city'])
        self.select_element(LoginFlowNavigationLocators.COUNTRY, 'by_text', cfg['country'])
        self.select_element(LoginFlowNavigationLocators.STATE, 'by_value', cfg['state'])
        self.input_data(LoginFlowNavigationLocators.ZIP, cfg['zip'])
        self.input_data(LoginFlowNavigationLocators.PHONE, cfg['phone'])

    def submit_button_to_register(self):
        self.click_element(LoginFlowNavigationLocators.SUBMIT_BUTTON)
