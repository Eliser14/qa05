# import time

from selenium.webdriver.common.by import By
from .base_page import *

LOGIN_BTN = (By.ID, "login-button")


class LoginPage(BasePage):

    ################################################################
    def should_be_login_form(self):
        self.should_be_login_box()
        self.should_be_login_btn()

    def should_be_login_box(self):
        assert self.d.find_elements(By.CLASS_NAME, "form_group")

    def should_be_login_btn(self):
        assert self.d.find_element(*LOGIN_BTN)

    ################################################################
    def signin_4_username(self, username, password):
        self.d.find_element(By.ID, "user-name").send_keys(username)
        self.d.find_element(By.ID, "password").send_keys(password)
        self.d.find_element(By.ID, "login-button").click()

    ################################################################

    def should_go_on_product_page(self):
        assert "inventory" in self.d.current_url

    def signin_standart_user(self, login="login", password="password"):
        username_input = self.d.find_element(By.ID, "user-name")
        username_input.send_keys(login)
        self.d.find_element(By.ID, "password").send_keys(password)
        self.d.find_element(*LOGIN_BTN).click()

    #
    def signin_locked_out_user(self, login="login", password="password"):
        self.d.find_element(By.ID, "user-name").send_keys(login)
        self.d.find_element(By.ID, "password").send_keys(password)
        self.d.find_element(*LOGIN_BTN).click()
        # self.d.implicitly_wait(2)
        message = self.d.find_element(By.XPATH, "//*[contains(text(), 'Epic sadface')]")
        value = message.text
        assert value == "Epic sadface: Sorry, this user has been locked out."

    def signin_empty_login_valid_password(self, password="password"):
        username_input = self.d.find_element(By.ID, "user-name")
        username_input.clear()
        password_input = self.d.find_element(By.ID, "password")
        password_input.send_keys(password)
        self.d.find_element(*LOGIN_BTN).click()
        message = self.d.find_element(By.XPATH, "//*[contains(text(), 'Epic sadface')]")
        value = message.text
        assert value == "Epic sadface: Username is required"


# class Credentials(BasePage):
#     login_list = ["standard_user", "problem_user", "performance_glitch_user"]
#     password = "secret_sauce"

# def signin_4_username(self, username, password):
#     self.d.find_element(By.ID, "user-name").send_keys(username)
#     self.d.find_element(By.ID, "password").send_keys(password)
#     self.d.find_element(By.ID, "login-button").click()
