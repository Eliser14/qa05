import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pages.base_page import *


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()


link_Main = "https://www.saucedemo.com/"


def test_user_can_signin(driver):
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
    time.sleep(2)
