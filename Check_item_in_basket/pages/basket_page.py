from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .locators import BasketPageLocators
from selenium.common.exceptions import TimeoutException

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        try:
            WebDriverWait(self.browser, 5).until(\
                EC.presence_of_element_located(BasketPageLocators.SUMMARY_BASKET_EMPTY))
        except TimeoutException:
            return True
        return False
