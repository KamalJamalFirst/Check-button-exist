import pytest
from .pages.main_page import MainPage
from .pages.base_page import BasePage

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
        page = MainPage(browser, link)
        page.open()
        login_page = page.go_to_login_page()
        login_page.should_be_login_page()

    def test_guest_should_see_login_link_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = BasePage(browser, link)
        page.open()
        page.should_be_login_link()
