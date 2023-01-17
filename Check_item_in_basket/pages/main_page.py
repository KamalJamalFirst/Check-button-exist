import time

from .base_page import BasePage
from .locators import MainPageLocators, PickedItemCharacteristics, MainPageMessagesBeforeAddingItem
from .catch_exceptions import CatchExceptions


class MainPage(BasePage):
    def go_to_basket_page(self):
        basket_link = self.browser.find_element(*MainPageLocators.ADD_TO_BASKET_BUTTON)
        basket_link.click()
        self.solve_quiz_and_get_code()


    def before_going_to_basket_define_messages_check(self):
        for a in MainPageMessagesBeforeAddingItem.count_locators_dict_for_messages(self):
            BasePage.is_element_present(
                self, *MainPageMessagesBeforeAddingItem.dict_for_massages[a].values(), a),\
                f"Field {MainPageMessagesBeforeAddingItem.dict_for_massages[a].keys()} didn't find"
        print(self.dict_for_compare)
        for b in PickedItemCharacteristics.count_dict_for_item(self):
            print(b)
            assert CatchExceptions.catch_exceptions_in_mainpage_messages(
                self, *PickedItemCharacteristics.dict_for_item[b].values(), b),\
                "Characteristic of the item don't match with the message after adding the item"

