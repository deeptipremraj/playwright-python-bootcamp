from playwright.sync_api import Locator

from autoexercise.pages.base_page import BasePage


class LoginPage(BasePage):
    path = "/login"

    @property
    def error_message(self) -> Locator:
        return self.page.get_by_text("Your email or password is incorrect!")

    def login(self, email: str, password: str) -> None:
        self.page.get_by_test_id("login-email").fill(email)
        self.page.get_by_test_id("login-password").fill(password)
        self.page.get_by_test_id("login-button").click()
