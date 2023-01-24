from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    SEE_EMPTY_BUSKET = (By.CSS_SELECTOR, '.basket-mini a.btn.btn')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    SUMMARY_BASKET_EMPTY = (By.CSS_SELECTOR, '#content_inner .basket_summary')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form.well')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form.well')
    REGISTER_USER_EMAIL = (By.CSS_SELECTOR, 'input#id_registration-email')
    REGISTER_USER_PW1 = (By.CSS_SELECTOR, 'input#id_registration-password1')
    REGISTER_USER_PW2 = (By.CSS_SELECTOR, 'input#id_registration-password2')
    BUTTON_SUBMIT_REGISTER = (By.CSS_SELECTOR, "button[name*='registration']")

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

class MainPageMessagesAfterAddingItem():
    dict_for_massages = {
        1: {'GENERAL_FIELD_FOR_MESSAGES': (By.CSS_SELECTOR, '#messages')},
        2: {'MESSAGE_WITH_PICKED_NAME_BOOK': (By.CSS_SELECTOR, '#messages > div:first-child strong')},
        3: {'MESSAGE_WITH_PICKED_PRICE_BOOK': (By.CSS_SELECTOR, '#messages > div:last-child strong')}
    }

    def count_locators_dict_for_messages(self):
        for key in MainPageMessagesAfterAddingItem.dict_for_massages:
            yield key
