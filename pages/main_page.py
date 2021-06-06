from .base_page import BasePage
from .locators import MainPageLocators, LoginPage
import time


class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login is not presented"

    def should_be_login_page(self):
        assert "login" in self.browser.current_url, "This is url not for login page"
        assert self.is_element_present(*LoginPage.should_be_login_form(LoginPage)), "There is no login form on this page"
        assert self.is_element_present(*LoginPage.should_be_register_form(LoginPage)), "There is no register form on this page"