from selenium.webdriver.common.by import By

# from selenium.webdriver.support.wait import WebDriverWait

from .base_page import *

CART_BTN = (By.ID, "shopping_cart_container")
BACKPACK_LABEL = (By.ID, "item_4_title_link")
BACKPACK_IMG = (By.ID, "item_4_img_link")
BACKPACK_ADD_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
BIKELIGHT_LABEL = (By.CSS_SELECTOR, "#item_0_title_link .inventory_item_name")
# BIKELIGHT_IMG =
# BIKELIGHT_ADD_BTN =


class InventoryPage(BasePage):
    def add_to_cart_backpack_inventory_item(self):
        self.d.find_element(*BACKPACK_ADD_BTN).click()
        assert "id=4" in self.d.current_url

    def add_to_cart_backpack_inventory(self):
        self.d.implicitly_wait(10)
        add_item = self.d.find_element(*BACKPACK_ADD_BTN)
        add_item.click()
        go_to_cart = self.d.find_element(*CART_BTN)
        go_to_cart.click()
        assert "cart" in self.d.current_url
        assert (
            "Sauce Labs Backpack"
            in self.d.find_element(By.ID, "item_4_title_link").text
        )

    def change_quantity_in_cart(self):
        self.add_to_cart_backpack_inventory()
