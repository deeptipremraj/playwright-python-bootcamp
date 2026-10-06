from playwright.sync_api import Locator

from autoexercise.pages.base_page import BasePage


class CartPage(BasePage):
    path = "/view_cart"

    @property
    def rows(self) -> Locator:
        return self.page.locator("#cart_info_table tbody tr")

    @property
    def item_names(self) -> Locator:
        return self.page.locator("#cart_info_table .cart_description h4 a")
