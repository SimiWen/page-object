""" 页面对象
"""

import abc
from .driver import WebElement


class PageObject:

    @abc.abstractmethod
    def __init__(self, driver):
        self.driver = driver
        self.locators = {}
        self.url = ''

    def open(self):
        self.driver.get(self.url)
        return self

    def close(self):
        self.driver.close()
        self.driver.quit()

    @property
    def title(self):
        return self.driver.title

    def element(self, locator):
        self.driver.wait_for_exist(self.locators[locator])
        return WebElement(self.driver.find_element_by_locator(self.locators[locator]))

    def elements(self, locator):
        self.driver.wait_for_exist(self.locators[locator])
        return [WebElement(e) for e in self.driver.find_elements_by_locator(self.locators[locator])]
