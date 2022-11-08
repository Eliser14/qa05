from selenium.webdriver.common.by import By
from .base_page import *


class LoginPage(BasePage):
    def register_standart_user(self, login="login", password="password"):
        login_input = self.driver.find_element(By.ID, "user-name")
        login_input.send_keys(login)
        password_input = self.driver.find_element(By.ID, "password")
        password_input.send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        assert "inventory" in self.driver.current_url
