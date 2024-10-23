from selenium.webdriver.remote.webdriver import WebDriver
from pages.locators import *


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page can not be opened for this page class')

    def verify_header_text(self, text):
        header_test_text = self.driver.find_element(*title_locator).text
        assert header_test_text == text, "The text in the header isn't correct"

    def find_and_scroll_to_element(self, locator):
        page_element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", page_element)
        return page_element

    def send_keys(self, locator, keys):
        element = self.find_and_scroll_to_element(locator)
        element.send_keys(keys)
