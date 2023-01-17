from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from math import log, sin
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, locators_type, key):
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(locators_type))
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
        WebDriverWait(self.browser, 5).until(EC.alert_is_present())
        try:
            self.browser.switch_to.alert
            alert_text = alert.text
            print(f'Your code: {alert_text}')
            alert.accept()
        except NoAlertPresentException:
            print('No second alert presented')

