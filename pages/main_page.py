from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import MainPageLocators

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK)