from pages.base_page import BasePage
from pages.locators import *


class EcoFriendly(BasePage):
    page_url = '/collections/eco-friendly.html'

    def verify_filter_title(self):
        filter_title = self.find_and_scroll_to_element(filter_header)
        assert filter_title.text == 'Shopping Options'

    def verify_item_is_presented(self):
        item = self.find_and_scroll_to_element(product_item)
        assert item.text == 'Ana Running Short'
