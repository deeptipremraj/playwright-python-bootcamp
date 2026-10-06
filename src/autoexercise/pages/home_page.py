from playwright.sync_api import Locator

from autoexercise.pages.base_page import BasePage


class HomePage(BasePage):
    path = "/"

    @property
    def featured_items(self) -> Locator:
        return self.page.locator(".features_items .product-image-wrapper")
