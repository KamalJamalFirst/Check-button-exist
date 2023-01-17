from .base_page import BasePage


class CatchExceptions(BasePage):
    def catch_exceptions_in_mainpage_messages(self, locator, number):
        define_text = self.browser.find_element(*locator)
        if self.dict_for_compare[number] == define_text.text:
            return True
        else:
            return False




