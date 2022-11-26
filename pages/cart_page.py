from selenium.webdriver.common.by import By
from .base_page import *

CART_ITEM = (By.CLASS_NAME, "cart_item")


class CartPage(BasePage):
    def backpack_can_be_removed(self):
        self.d.find_element(By.ID, "remove-sauce-labs-backpack").click()

    def cart_is_empty(self):
        assert self.element_is_NOT_present(*CART_ITEM)
