from pages.base_page import BasePage
from pages.locators import *


class Sale(BasePage):
    page_url = '/sale.html'

    def verify_comparing(self, text):
        compare_title = self.find_and_scroll_to_element(compare_products)
        assert compare_title.text == text

    def verify_whats_new(self, text):
        compare_title = self.find_and_scroll_to_element(whats_new)
        assert compare_title.text == text
