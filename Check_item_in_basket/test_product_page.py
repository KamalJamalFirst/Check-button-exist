import pytest

from .pages.main_page import MainPage

def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = MainPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    page.go_to_basket_page()
    page.before_going_to_basket_define_messages_check()

@pytest.mark.xfail(reason='Correct work - negative test')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.guest_cant_see_success_message_after_adding_product_to_basket()

@pytest.mark.xfail(reason='Correct work - negative test')
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.message_disappeared_after_adding_product_to_basket()
