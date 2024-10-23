from pages.base_page import BasePage
from pages.locators import *


class AccountCreate(BasePage):
    page_url = '/customer/account/create/'

    def fill_form(self, first_name, last_name, email_address, password):
        self.send_keys(first_name_locator, first_name)
        self.send_keys(last_name_locator, last_name)
        self.send_keys(email_locator, email_address)
        self.send_keys(password_locator, password)
        self.send_keys(password_confirmation_locator, password)

    def submit_form(self):
        submit_button = self.find_and_scroll_to_element(submit_button_locator)
        submit_button.click()

    def verify_valid_form(self):
        assert self.driver.current_url == 'https://magento.softwaretestingboard.com/customer/account/'

    def verify_invalid_form(self, text):
        first_name_error = self.find_and_scroll_to_element(error_first_name_locator)
        assert first_name_error.text == text
