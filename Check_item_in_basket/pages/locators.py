from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "[class*='btn-add-to-basket']")

class PickedItemCharacteristics():
    dict_for_item = {
        2: {'book title': (By.CSS_SELECTOR, 'div[class="col-sm-6 product_main"] > h1')},
        3: {'book price': (By.CSS_SELECTOR, 'div[class="col-sm-6 product_main"] > p')}
    }

    def count_dict_for_item(self):
        for item in PickedItemCharacteristics.dict_for_item.keys():
            yield item

class MainPageMessagesBeforeAddingItem():
    dict_for_massages = {
        1: {'GENERAL_FIELD_FOR_MESSAGES': (By.CSS_SELECTOR, '#messages')},
        2: {'MESSAGE_WITH_PICKED_NAME_BOOK': (By.CSS_SELECTOR, '#messages > div:first-child strong')},
        3: {'MESSAGE_WITH_PICKED_PRICE_BOOK': (By.CSS_SELECTOR, '#messages > div:last-child strong')}
    }

    def count_locators_dict_for_messages(self):
        for key in MainPageMessagesBeforeAddingItem.dict_for_massages:
            yield key
