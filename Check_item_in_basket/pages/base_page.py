from selenium.common.exceptions import NoSuchElementException, TimeoutException
from math import log, sin
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def should_be_authorized_user(self):
        assert self.is_element_present(BasePageLocators.USER_ICON), "User icon is not presented,\
                                                                      probably unauthorised user"

    def should_be_login_link(self):
        try:
            WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(BasePageLocators.LOGIN_LINK))
        except NoSuchElementException:
            "Login link is not presented"
        return True

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, locators_type, key=0):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(locators_type))
        try:
            locator = self.browser.find_element(*locators_type)
            locator_text = locator.text
            self.dict_for_compare[key] = locator_text
        except AttributeError:
            self.dict_for_compare = {}
            self.dict_for_compare[key] = locator_text
            return True
        except NoSuchElementException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(' ')[2]
        answer = str(log(abs((12 * sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            WebDriverWait(self.browser, 5).until(EC.alert_is_present())
            self.browser.switch_to.alert
            alert_text = alert.text
            print(f'Your code: {alert_text}')
            alert.accept()
        except:
            print('No second alert presented')

    def is_not_element_present(self, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located(locator))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located(locator))
        except TimeoutException:
            return False
        return True
