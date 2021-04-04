import os

from resources.locators.locatorsLoginPage import Locators
from resources.pageObjects.basePage import BasePage


class LoginPage(BasePage):
    URL = os.getenv('E2E_URL', 'https://www.morele.net/login')

    def __init__(self, context):
        super().__init__(context)
        self.logger = context.logger
        self.open()

    def login_as(self, **kwargs):
        """Login to Morele using the credentials passed"""
        self.logger.info('Login to Morele')
        self.clear_and_enter_text(Locators.LOGIN_USERNAME_INPUT, kwargs['username'])

        self.driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).clear()
        self.clear_and_enter_text(Locators.LOGIN_PASSWORD_INPUT, kwargs['password'])

        self.click(Locators.LOGIN_SUBMIT_BUTTON)
        return self

    def enter_username(self, username):
        self.clear_and_enter_text(Locators.LOGIN_USERNAME_INPUT, username, 15)

    def enter_password(self, password):
        self.clear_and_enter_text(Locators.LOGIN_PASSWORD_INPUT, password, 15)

    def is_login_successful(self):
        return self.wait_for_element(Locators.LOGIN_PAGE_ASSERTION)

    def is_login_failed(self):
        return self.wait_for_element_to_be_not_clickable(Locators.LOGIN_PAGE_ASSERTION)