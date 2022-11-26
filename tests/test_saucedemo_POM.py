# import time
import pytest

from pages.login_page import *
from pages.inventory_page import *
from pages.cart_page import *
from selenium.webdriver.support.select import Select

link_Main = "https://www.saucedemo.com/"
link_inv = "https://www.saucedemo.com/inventory.html"
link_Cart = "https://www.saucedemo.com/cart.html"


# def test_standart_user_can_signin(driver):
#     page = BasePage(driver, link_Main)
#     page.open_page()
#     assert driver.title == "Swag Labs"
#     page = LoginPage(driver, link_Main)
#     page.should_be_login_form()
#     page.signin_standart_user(login="standard_user", password="secret_sauce")
#     page.should_go_on_product_page()
#     # time.sleep(2)
#
#
# def test_locked_out_user(d):
#     page = BasePage(d, link_Main)
#     page.open_page()
#     assert d.title == "Swag Labs"
#     page = LoginPage(d, link_Main)
#     page.should_be_login_form()
#     # time.sleep(1)
#     page.signin_locked_out_user(login="locked_out_user", password="secret_sauce")
#     # time.sleep(1)
#
#
# def test_empty_login_valid_password(driver):
#     page = BasePage(driver, link_Main)
#     page.open_page()
#     page = LoginPage(driver, link_Main)
#     page.should_be_login_form()
#     page.signin_empty_login_valid_password()
#     time.sleep(2)

# @pytest.mark.parametrize(
#     "username,password",
#     [
#         ("standard_user", "secret_sauce"),
#         ("problem_user", "secret_sauce"),
#         ("performance_glitch_user", "secret_sauce"),
#         pytest.param("locked_out_user", "secret_sauce", marks=pytest.mark.xfail),
#     ],
# )
# def test_signin_4_username(d, username, password):
#     page = LoginPage(d, link_Main)
#     page.should_be_login_form()
#     page.signin_4_username(username, password)
#     page.should_go_on_product_page()


# def test_login_from_list(d):
#     # username = (Credentials.login_list)
#     # page = LoginPage(d, link_Main)
#     # page.should_be_login_form()
#     for name in Credentials.login_list:
#         d.get("https://www.saucedemo.com/")
#         page = LoginPage(d, link_Main)
#         page.signin_standart_user(name, password='secret_sauce')
#         page.should_go_on_product_page()
#         time.sleep(2)
# yield d
# d.quit()
@pytest.mark.order(1)
def test_signin_using_a_list_of_credentials(d, login_from_list):
    assert d.title == "Swag Labs"
    # page = LoginPage(d, link_Main)
    assert "inventory" in d.current_url
    # time.sleep(2)


# poetry run pytest tests/test_saucedemo_POM.py::test_signin_using_a_list_of_credentials -v -s -n auto


@pytest.mark.parametrize(
    "username,password",
    [
        ("", ""),
        ("standartUser", "secret_sauce"),
        ("standard_user", "secretsauce"),
        ("standard_user", ""),
        ("", "secret_sauce"),
        ("locked_out_user", "secret_sauce"),
    ],
)
@pytest.mark.order(4)
def test_negativ_signin(d, username, password):
    page = LoginPage(d, link_Main)
    page.should_be_login_form()
    page.signin_4_username(username, password)
    assert d.find_element(By.XPATH, "//*[contains(text(), 'Epic sadface')]")


# def test_add_items(d):
#     page = LoginPage(d, link_Main)
#     page.signin_standart_user(login="problem_user", password="secret_sauce")
#     page = InventoryPage(d, link_inv)
#     page.add_to_cart_backpack_inventory()


@pytest.mark.order(2)
@pytest.mark.xfail
def test_add_items(d, login_from_list):
    page = InventoryPage(d, link_inv)
    d.implicitly_wait(2)
    page.add_to_cart_backpack_inventory()


# poetry run pytest tests/test_saucedemo_POM.py::test_add_items -v -n auto
# def test_remove_items_from_cart_on_cart_page(d):
#     page = BasePage(d, link_Main)
#     page.open_page()
#     page = LoginPage(d, link_Main)
#     page.signin_standart_user(login="standard_user", password="secret_sauce")
#     page = InventoryPage(d, link_inv)
#     page.add_to_cart_backpack_inventory()
#     time.sleep(2)
#     page = CartPage(d, link_Cart)
#     page.backpack_can_be_removed()
#     page.cart_is_empty()
@pytest.mark.order(3)
@pytest.mark.xfail
def test_remove_items_from_cart_on_cart_page(d, login_from_list):
    page = InventoryPage(d, link_inv)
    page.add_to_cart_backpack_inventory()
    page = CartPage(d, link_Cart)
    d.implicitly_wait(2)
    page.backpack_can_be_removed()
    page.cart_is_empty()


# poetry run pytest tests/test_saucedemo_POM.py::test_remove_items_from_cart_on_cart_page -v -n auto
