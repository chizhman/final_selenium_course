from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    SWITCH_TO_BASKET = (By.CSS_SELECTOR, ".basket-mini a.btn.btn-default")


class LoginPage(BasePage):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

