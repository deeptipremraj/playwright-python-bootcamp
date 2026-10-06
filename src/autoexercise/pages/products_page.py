from playwright.sync_api import Locator

from autoexercise.pages.base_page import BasePage


class ProductsPage(BasePage):
    path = "/products"

    @property
    def cards(self) -> Locator:
        return self.page.locator(".features_items .product-image-wrapper")

    @property
    def names(self) -> Locator:
        return self.page.locator(".features_items .productinfo p")

    @property
    def searched_heading(self) -> Locator:
        return self.page.get_by_role("heading", name="Searched Products")

    def search(self, term: str) -> None:
        self.page.locator("#search_product").fill(term)
        self.page.locator("#submit_search").click()

    def add_to_cart(self, index: int = 0) -> None:
        """Hover the card so the overlay button appears, click it, close the dialog."""
        card = self.cards.nth(index)
        card.hover()
        card.locator(".product-overlay .add-to-cart").click()
        self.page.locator("#cartModal .close-modal").click()
