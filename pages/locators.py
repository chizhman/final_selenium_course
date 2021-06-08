from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    SWITCH_TO_BASKET = (By.CSS_SELECTOR, ".basket-mini a.btn.btn-default")


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert True

    def should_be_login_form(self):
        LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
        assert True
        return LOGIN_FORM

    def should_be_register_form(self):
        REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
        assert True
        return REGISTER_FORM
