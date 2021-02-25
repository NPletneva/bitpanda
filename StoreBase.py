# -*- coding: UTF-8 -*-
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
import logging
from contextlib import contextmanager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support.ui import Select
import config

cfg = config.get_common_configs()


class StoreBase:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = cfg["base_url"]
        self.logger = logging.getLogger(__name__)

    def find_element(self, locator, time=10) -> object:
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_main_page(self):
        return self.driver.get(self.base_url)

    def get_current_url(self):
        return self.driver.current_url

    def select_element(self, locator, option, data):
        if option == 'by_text':
            Select(self.find_element(locator)).select_by_visible_text(data)
        if option == 'by_value':
            Select(self.find_element(locator)).select_by_value(data)

    def input_data(self, locator, data):
        self.find_element(locator).send_keys(data)

    def click_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.element_to_be_clickable(locator)).click()

    def get_attr(self, locator, option):
        return self.find_element(locator).get_attribute(option)

    def hover(self, locator):
        ActionChains(self.driver).move_to_element(self.find_element(locator)).perform()

    @contextmanager
    def wait_for_page_load(self, element, timeout=30):
        old_page = self.find_element(locator=element)
        yield
        WebDriverWait(self.driver, timeout).until(staleness_of(old_page))
