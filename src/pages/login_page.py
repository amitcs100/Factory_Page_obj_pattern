from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def login(self, username, password):
        self.enter_text(*self.USERNAME_FIELD, value=username)
        self.enter_text(*self.PASSWORD_FIELD, value=password)
        self.click(*self.LOGIN_BUTTON)
