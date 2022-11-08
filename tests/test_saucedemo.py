import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import *
from pages.inventory_page import *


@pytest.fixture(scope="function")  ####### for github actions
def driver():
    o = webdriver.ChromeOptions()
    o.headless = True
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=o
    )
    yield driver
    driver.quit()


# @pytest.fixture(scope="function")  ###### for pycharm
# def driver():
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     yield driver
#     driver.quit()


link_Main = "https://www.saucedemo.com/"
link_inv = "https://www.saucedemo.com/inventory.html"


def test_standart_user_can_signin(driver):
    # page = BasePage(browser, link_Main)
    # page.open_page()
    driver.get(link_Main)
    assert driver.title == "Swag Labs"
    login_input = driver.find_element(By.ID, "user-name")
    login_input.send_keys("standard_user")
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("secret_sauce")
    time.sleep(2)
    driver.find_element(By.ID, "login-button").click()
    assert "inventory" in driver.current_url
    # time.sleep(2)


def test_locked_out_user(driver):
    driver.get(link_Main)
    assert driver.title == "Swag Labs"
    login_input = driver.find_element(By.ID, "user-name")
    login_input.send_keys("locked_out_user")
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    driver.implicitly_wait(2)
    message = driver.find_element(By.XPATH, "//*[contains(text(), 'Epic sadface')]")
    value = message.text
    assert value == "Epic sadface: Sorry, this user has been locked out."


def test_add_items(driver):
    page = BasePage(driver, link_Main)
    page.open_page()
    page = LoginPage(driver, link_Main)
    page.register_standart_user(login="standard_user", password="secret_sauce")
    time.sleep(2)
    page = InventoryPage(driver, link_inv)
    page.add_to_cart_backpack_inventory()
    time.sleep(2)
