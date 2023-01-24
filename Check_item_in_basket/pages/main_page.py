from .base_page import BasePage
from .locators import MainPageLocators, PickedItemCharacteristics, MainPageMessagesAfterAddingItem
from .catch_exceptions import CatchExceptions
from .locators import BasePageLocators
from .login_page import LoginPage
from .basket_page import BasketPage


class MainPage(BasePage):

    def should_not_be_success_message(self):
        assert MainPage.is_not_element_present(self, *MainPageMessagesAfterAddingItem.dict_for_massages[2].values()),\
            "Success message is presented, but should not be"

    def guest_cant_see_success_message_after_adding_product_to_basket(self):
        assert MainPage.is_not_element_present(self, *MainPageMessagesAfterAddingItem.dict_for_massages[2].values()),\
            "Success message is presented and must be presented"

    def message_disappeared_after_adding_product_to_basket(self):
        assert BasePage.is_disappeared(self, *MainPageMessagesAfterAddingItem.dict_for_massages[2].values()),\
            "Message isn't disappeared"

    def go_to_basket_page(self):
        basket_link = self.browser.find_element(*MainPageLocators.ADD_TO_BASKET_BUTTON)
        basket_link.click()
        self.solve_quiz_and_get_code()

    def go_to_empty_basket_page(self):
        empty_basket_link = self.browser.find_element(*BasePageLocators.SEE_EMPTY_BUSKET)
        empty_basket_link.click()
        return BasketPage(browser=self.browser, url=self.browser.current_url)

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def before_going_to_basket_define_messages_check(self):
        for a in MainPageMessagesAfterAddingItem.count_locators_dict_for_messages(self):
            BasePage.is_element_present(
                self, *MainPageMessagesAfterAddingItem.dict_for_massages[a].values(), a),\
                f"Field {MainPageMessagesAfterAddingItem.dict_for_massages[a].keys()} didn't find"
        print(self.dict_for_compare)
        for b in PickedItemCharacteristics.count_dict_for_item(self):
            print(b)
            assert CatchExceptions.catch_exceptions_in_mainpage_messages(
                self, *PickedItemCharacteristics.dict_for_item[b].values(), b),\
                "Characteristic of the item don't match with the message after adding the item"

