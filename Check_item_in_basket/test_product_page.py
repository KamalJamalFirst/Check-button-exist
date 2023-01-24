import pytest
from .pages.main_page import MainPage

@pytest.mark.guest_basket
class TestGuestCheckBasketFromMainPage():
    def test_guest_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
        page = MainPage(browser, link)
        page.open()
        page.should_not_be_success_message()
        page.go_to_basket_page()
        page.before_going_to_basket_define_messages_check()

    @pytest.mark.xfail(reason='Correct work - negative test')
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
        page = MainPage(browser, link)
        page.open()
        page.go_to_basket_page()
        page.guest_cant_see_success_message_after_adding_product_to_basket()

    @pytest.mark.xfail(reason='Correct work - negative test')
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
        page = MainPage(browser, link)
        page.open()
        page.go_to_basket_page()
        page.message_disappeared_after_adding_product_to_basket()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
        page = MainPage(browser, link)
        page.open()
        empty_basket = page.go_to_empty_basket_page()
        empty_basket.should_be_empty_basket()

@pytest.mark.user_basket
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
        page = MainPage(browser, link)
        page.open()
        login_page = page.go_to_login_page()
        login_page.should_be_login_page()
        login_page = login_page.register_new_user()
        login_page.should_be_authorized_user()
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
        page = MainPage(browser, link)
        page.open()
        page.should_not_be_success_message()
        page.go_to_basket_page()
        page.before_going_to_basket_define_messages_check()

    @pytest.mark.xfail(reason='Correct work - negative test')
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
        page = MainPage(browser, link)
        page.open()
        page.go_to_basket_page()
        page.guest_cant_see_success_message_after_adding_product_to_basket()