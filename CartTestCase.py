# -*- coding: UTF-8 -*-
import logging
import re

import config
from StoreBase import StoreBase
from selenium.webdriver.common.by import By

# configuration
logger = logging.getLogger(__name__)
cfg = config.get_common_configs()


class CartLocators:
    ORDER_STEPS_MENU = (By.XPATH, "//*[@id='order_step']/li")
    ORDER_DETAIL_CONTENT = (By.XPATH, "//*[@id='cart_summary']//th")
    PRICE = (By.XPATH, "//*[@id='total_price']")
    DELIVERY_ADDRESS = (By.XPATH, "//*[@class='address first_item item box']")
    INVOICE_ADDRESS = (By.XPATH, "//*[@class='address last_item alternate_item box']")
    SUBMIT_BUTTON = (By.XPATH, "//*[@class='cart_navigation clearfix']//*[@title='Proceed to checkout']")
    QUANTITY = (By.XPATH, "//*[@id='summary_products_quantity']")
    DELETE = (By.CSS_SELECTOR, ".cart_quantity_delete")
    ALERT_CART_EMPTY = (By.XPATH, "//*[@id='center_column']/p")


class CartHelper(StoreBase):

    def __init__(self, driver):
        super().__init__(driver)

    def verify_cart(self, num):
        assert len(self.find_elements(CartLocators.ORDER_STEPS_MENU)) == 5
        assert len(self.find_elements(CartLocators.ORDER_DETAIL_CONTENT)) == 7
        QUANTITY_TEXT = self.find_element(CartLocators.QUANTITY).text
        assert re.match((r"%s\sProducts?" % num), QUANTITY_TEXT)
        self.find_element(CartLocators.DELIVERY_ADDRESS)
        self.find_element(CartLocators.INVOICE_ADDRESS)

    def delete_product_from_cart(self):
        self.click_element(CartLocators.DELETE)

    def verify_cart_empty(self):
        self.wait_for_page_load(CartLocators.ORDER_DETAIL_CONTENT)
        self.find_element(CartLocators.ALERT_CART_EMPTY)

