"""Base class for page objects and the shared navigation bar."""

from playwright.sync_api import Locator, Page


class NavBar:
    def __init__(self, page: Page):
        self.page = page

    @property
    def login_link(self) -> Locator:
        return self.page.locator('header a[href="/login"]')

    @property
    def logout_link(self) -> Locator:
        return self.page.locator('header a[href="/logout"]')

    @property
    def logged_in_as(self) -> Locator:
        return self.page.locator("header").get_by_text("Logged in as")

    @property
    def products_link(self) -> Locator:
        return self.page.locator('header a[href="/products"]')


class BasePage:
    path = "/"

    def __init__(self, page: Page):
        self.page = page
        self.nav = NavBar(page)

    def open(self):
        self.page.goto(self.path)
        return self
