import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    o = webdriver.ChromeOptions()
    o.headless = True
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=o
    )
    yield driver
    driver.quit()


# @pytest.mark.parametrize("test_input,expected",
#     [("3+5", 8), ("2+4", 6), pytest.param("6*9", 42, marks=pytest.mark.xfail)],)
# def test_eval(test_input, expected):
#     assert eval(test_input) == expected

# @pytest.fixture(scope="function",
#                 params=["login,password",
#                          [("standard_user", "secret_sauce"),
#                           ("problem_user", "secret_sauce"),
#                           ("performance_glitch_user", "secret_sauce"),
#                           pytest.param("locked_out_user", "secret_sauce", marks=pytest.mark.xfail)]])
# def signin4(driver, login, password):
#     driver.get("https://www.saucedemo.com/")
#     username_input = driver.find_element(By.ID, "user-name")
#     username_input.send_keys(login)
#     password_input = driver.find_element(By.ID, "password")
#     password_input.send_keys(password)
#     driver.find_element(By.ID, "login-button").click()


@pytest.mark.parametrize(
    "login,password",
    [
        ("standard_user", "secret_sauce"),
        ("problem_user", "secret_sauce"),
        ("performance_glitch_user", "secret_sauce"),
        pytest.param("locked_out_user", "secret_sauce", marks=pytest.mark.xfail),
    ],
)
def test_signin(driver, login, password):
    driver.get("https://www.saucedemo.com/")
    username_input = driver.find_element(By.ID, "user-name")
    username_input.send_keys(login)
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys(password)
    driver.find_element(By.ID, "login-button").click()
