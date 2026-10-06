"""UI fixtures: ad blocking and page objects."""

import re

import pytest

from autoexercise.pages.cart_page import CartPage
from autoexercise.pages.home_page import HomePage
from autoexercise.pages.login_page import LoginPage
from autoexercise.pages.products_page import ProductsPage

AD_HOSTS = re.compile(
    r"(googlesyndication|doubleclick|googleadservices|adservice\.google|"
    r"googletagmanager|google-analytics|fundingchoices|adsbygoogle)"
)

HIDE_ADS_CSS = """
(() => {
  const css = `ins.adsbygoogle, iframe[id^="aswift"], iframe[id^="google_ads"],
    #google_vignette, .fc-consent-root, #ad_position_box { display: none !important; }`;
  const add = () => {
    const style = document.createElement("style");
    style.textContent = css;
    document.documentElement.appendChild(style);
  };
  if (document.documentElement) add();
  else document.addEventListener("DOMContentLoaded", add);
})();
"""


@pytest.fixture
def page(page):
    """Wraps the pytest-playwright page: block ad requests and hide ad overlays.

    Ads on this site can cover buttons and break clicks, so every UI test gets this.
    """
    page.context.route(AD_HOSTS, lambda route: route.abort())
    page.context.add_init_script(HIDE_ADS_CSS)
    return page


@pytest.fixture
def home_page(page) -> HomePage:
    return HomePage(page).open()


@pytest.fixture
def login_page(page) -> LoginPage:
    return LoginPage(page).open()


@pytest.fixture
def products_page(page) -> ProductsPage:
    return ProductsPage(page).open()


@pytest.fixture
def cart_page(page) -> CartPage:
    return CartPage(page)
