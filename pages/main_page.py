from pages.base_page import BasePage
from pages.locators import MainPageLocators
from pages.login_page import LoginPage

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        #return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK)

    def go_to_basket(self):
        button = self.browser.find_element(*MainPageLocators.BASKET_BUTTON)
        button.click()

    def should_not_be_items(self):
        assert self.is_not_element_present(*MainPageLocators.BASKET_ITEMS)

    def message_empty_is_visible(self):
        assert self.browser.find_element(*MainPageLocators.BASKET_EMPTY)

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)