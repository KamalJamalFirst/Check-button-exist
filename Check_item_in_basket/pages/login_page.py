from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.url, 'We are not in the login page'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert BasePage.is_element_present(self, LoginPageLocators.LOGIN_FORM), "Login form didn't find"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert BasePage.is_element_present(self, LoginPageLocators.REGISTER_FORM), "Register form didn't find"

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        register_login = self.browser.find_element(*LoginPageLocators.REGISTER_USER_EMAIL)
        register_pw1 = self.browser.find_element(*LoginPageLocators.REGISTER_USER_PW1)
        register_pw2 = self.browser.find_element(*LoginPageLocators.REGISTER_USER_PW2)
        register_submit = self.browser.find_element(*LoginPageLocators.BUTTON_SUBMIT_REGISTER)
        register_login.send_keys(email)
        register_pw1.send_keys(password)
        register_pw2.send_keys(password)
        register_submit.click()
        return BasePage(browser=self.browser, url=self.browser.current_url)
