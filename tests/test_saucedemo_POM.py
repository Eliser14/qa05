import time
from pages.login_page import *
from pages.inventory_page import *
from pages.cart_page import *


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
# def test_locked_out_user(driver):
#     page = BasePage(driver, link_Main)
#     page.open_page()
#     assert driver.title == "Swag Labs"
#     page = LoginPage(driver, link_Main)
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
def test_signin_4_username(driver, login, password):
    page = BasePage
    page.open_page()
    page = LoginPage
    page.should_be_login_form()
    page.signin_4_username()
    page.should_go_on_product_page()


def test_add_items(driver):
    page = BasePage(driver, link_Main)
    page.open_page()
    page = LoginPage(driver, link_Main)
    page.signin_standart_user(login="standard_user", password="secret_sauce")
    # time.sleep(2)
    page = InventoryPage(driver, link_inv)
    page.add_to_cart_backpack_inventory()
    # time.sleep(2)


def test_remove_items_from_cart_on_cart_page(driver):
    page = BasePage(driver, link_Main)
    page.open_page()
    page = LoginPage(driver, link_Main)
    page.signin_standart_user(login="standard_user", password="secret_sauce")
    page = InventoryPage(driver, link_inv)
    page.add_to_cart_backpack_inventory()
    time.sleep(2)
    page = CartPage(driver, link_Cart)
    page.backpack_can_be_removed()
    page.cart_is_empty()
