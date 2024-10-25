from pages.base_page import BasePage
from pages.locators import *


class EcoFriendly(BasePage):
    page_url = '/collections/eco-friendly.html'

    def verify_sorting(self, text):
        filter_title = self.find_and_scroll_to_element(sorting_title)
        assert filter_title.text == text

    def verify_item_is_presented(self, text):
        item = self.find_and_scroll_to_element(product_item)
        assert item.text == text
