"""
WebDriver, WebElement 二次封装
"""

import time
from selenium.webdriver.remote.webdriver import WebDriver as SeleniumWebDriver
from selenium.webdriver.remote.webelement import WebElement as SeleniumWebElement
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

LOCATOR = {
    'id': By.ID,
    'name': By.NAME,
    'class': By.CLASS_NAME,
    'link': By.LINK_TEXT,
    'p-link': By.PARTIAL_LINK_TEXT,
    'tag': By.TAG_NAME,
    'xpath': By.XPATH,
    'css': By.CSS_SELECTOR
}


class WebDriver(SeleniumWebDriver):
    def __init__(self, **kwargs):
        super(WebDriver, self).__init__(**kwargs)

    def find_element_by_locator(self, locator):
        """
        :Usage:
            driver.find_elements_by_locator('id=username').send_keys('name')
        """
        locator_type, locator_value = locator.split('=', maxsplit=1)
        # element = self.find_element(by=LOCATOR[locator_type], value=locator_value)
        # return WebElement(element)
        return self.find_element(by=LOCATOR[locator_type], value=locator_value)

    def find_elements_by_locator(self, locator):
        """
        :Usage:
            elements = driver.find_elements_by_locator('class=somethings')
        """
        locator_type, locator_value = locator.split('=', maxsplit=1)
        return self.find_elements(by=LOCATOR[locator_type], value=locator_value)

    def is_element_exist(self, locator):
        """
        :Usage:
            if driver.is_element_exist():
                element = driver.find_element_by_locator('id=something')
        """
        try:
            self.find_element_by_locator(locator)
            return True
        except exceptions.NoSuchElementException:
            return False

    def wait_for_exist(self, locator, wait_frequency=20, wait_second=.5):
        """
        :Usage:
            driver.wait_for_exist('id=something')
        """
        for _ in range(wait_frequency):
            if self.is_element_exist(locator):
                return
            time.sleep(wait_second)
        else:
            raise exceptions.TimeoutException(f'wait for {wait_frequency * wait_second}s but element does not exist')


class WebElement(SeleniumWebElement):
    def __init__(self, locator):
        super(WebElement, self).__init__(locator.parent, locator.id)

    @property
    def text(self):
        return super(WebElement, self).text

    @text.setter
    def text(self, value):
        """
        :Usage:
            element.text = 'test'
        """
        self.clear()
        self.send_keys(value)

    def select(self, value_or_text):
        """
        :Usage:
            element.select(0)
            element.select('some-text')
        """
        if isinstance(value_or_text, int):
            Select(self).select_by_index(value_or_text)
        elif isinstance(value_or_text, str):
            Select(self).select_by_index(value_or_text)
        else:
            raise TypeError(f'select does not support "{type(value_or_text)}"')

    def hover(self, driver):
        """
        :Usage:
            element.hover(driver)
        """
        ActionChains(driver).move_to_element(self).perform()

    def find_element_by_locator(self, locator):
        """
        :Usage:
            element.find_elements_by_locator('id=username').send_keys('name')
        """
        locator_type, locator_value = locator.split('=', maxsplit=1)
        element = self.find_element(by=LOCATOR[locator_type], value=locator_value)
        return WebElement(element)

    def find_elements_by_locator(self, locator):
        """
        :Usage:
            elements = element.find_elements_by_locator('class=somethings')
        """
        locator_type, locator_value = locator.split('=', maxsplit=1)
        elements = self.find_elements(by=LOCATOR[locator_type], value=locator_value)
        return [WebElement(e) for e in elements]

    def wait_for_displayed(self, wait_frequency=20, wait_second=.5):
        """
        :Usage:
            element.wait_for_displayed()
        """
        for i in range(wait_frequency):
            if self.is_displayed():
                return
            time.sleep(wait_second)
        else:
            raise exceptions.TimeoutException(f'wait for {wait_frequency * wait_second}s but element does not display')
