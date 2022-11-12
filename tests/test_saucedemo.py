import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")  ####### for github actions
def driver():
    o = webdriver.ChromeOptions()
    o.headless = True
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=o
    )
    yield driver
    driver.quit()


link_Main = "https://www.saucedemo.com/"
link_inv = "https://www.saucedemo.com/inventory.html"


def test_standart_user_can_signin(driver):
    driver.get(link_Main)
    assert driver.title == "Swag Labs"
    login_input = driver.find_element(By.ID, "user-name")
    login_input.send_keys("standard_user")
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("secret_sauce")
    # time.sleep(2)
    driver.find_element(By.ID, "login-button").click()
    assert "inventory" in driver.current_url


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
    driver.get(link_Main)
    assert driver.title == "Swag Labs"
    login_input = driver.find_element(By.ID, "user-name")
    login_input.send_keys("standard_user")
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("secret_sauce")
    time.sleep(2)
    driver.find_element(By.ID, "login-button").click()
    assert "inventory" in driver.current_url
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "shopping_cart_container").click()
    assert "cart" in driver.current_url
    assert "Sauce Labs Backpack" in driver.find_element(By.ID, "item_4_title_link").text
    time.sleep(2)
