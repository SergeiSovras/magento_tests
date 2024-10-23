from pages.base_page import BasePage
from pages.locators import *


class Sale(BasePage):
    page_url = '/sale.html'

    def verify_comparing(self):
        compare_title = self.find_and_scroll_to_element(compare_products)
        assert compare_title.text == 'Compare Products'

    def verify_whats_new(self):
        compare_title = self.find_and_scroll_to_element(whats_new)
        assert compare_title.text == "What's New"
