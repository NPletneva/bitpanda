# -*- coding: UTF-8 -*-
import logging

import config
from StoreBase import StoreBase
from selenium.webdriver.common.by import By

# configuration
logger = logging.getLogger(__name__)
cfg = config.get_common_configs()


class CatalogLocators:
    DRESSES_SECTION = (By.XPATH, "//*[@id='block_top_menu']/ul/li[2]")
    SUMMER_DRESSES = (By.XPATH, "//*[@id='block_top_menu']/ul/li[2]/ul/li[3]")
    FIRST_PRODUCT_ADD_TO_CART = (By.XPATH, "//*[@class='product_list row list']/li[1]//*[@rel='nofollow']")
    PAGE_HEADER = (By.XPATH, "//*[contains(@class, 'page-heading')]")
    LIST_VIEW = (By.XPATH, "//*[contains(@id, 'list')]")
    PRODUCT_ADDED_POPUP = (By.XPATH, "//*[@id='layer_cart']")
    CHECKOUT_BUTTON = (By.XPATH, "//*[@id='layer_cart']//*[@href]")


class CatalogHelper(StoreBase):

    def __init__(self, driver):
        super().__init__(driver)

    def open_summer_dresses_section(self):
        self.hover(CatalogLocators.DRESSES_SECTION)
        self.click_element(CatalogLocators.SUMMER_DRESSES)

    def set_list_view(self):
        self.click_element(CatalogLocators.LIST_VIEW)

    def add_product_to_cart(self):
        self.find_element(CatalogLocators.FIRST_PRODUCT_ADD_TO_CART)
        self.click_element(CatalogLocators.FIRST_PRODUCT_ADD_TO_CART)

    def proceed_to_checkout(self):
        self.find_element(CatalogLocators.PRODUCT_ADDED_POPUP)
        self.click_element(CatalogLocators.CHECKOUT_BUTTON)
        self.wait_for_page_load(CatalogLocators.PRODUCT_ADDED_POPUP)
        logger.info('order page %s is loaded' % self.get_current_url())