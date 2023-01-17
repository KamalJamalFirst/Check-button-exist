from .pages.main_page import MainPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = MainPage(browser, link)
    page.open()
    basket_page = page.go_to_basket_page()
    # time.sleep(1200)
    page.before_going_to_basket_define_messages_check()

