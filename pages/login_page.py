import time

from pages.base_page import BasePage
from pages.locators import LoginPageLocators, MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login" in self.browser.current_url

    def should_be_login_form(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        assert True

    def should_be_register_form(self):
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        assert True

    def register_new_user(self,):
        email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email.send_keys(str(time.time()) + "@fakemail.org")
        password = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password.send_keys("PanchoMAN4490")
        confirm_password = self.browser.find_element(*LoginPageLocators.CONFIRM_REGISTER_PASSWORD)
        confirm_password.send_keys("PanchoMAN4490")
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
