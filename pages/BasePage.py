import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    PATH = ""
    ALERT = (By.CSS_SELECTOR, "div.alert")

    def __init__(self, browser):
        self.browser = browser

        # self.logger = logging.getLogger(self.browser.test_name)
        # self.logger = logging.getLogger(str(self))
        # logging.getLogger(str(self))
        # file_handler = logging.FileHandler(f"logs/{self.browser.test_file}.log")
        # file_handler.setFormatter(logging.Formatter("%(asctime)s - %(funcName)s [%(module)s] %(name)s | %(levelname)s :  %(message)s"))
        # # self.logger.addHandler(file_handler)
        # # self.logger.setLevel(level=self.browser.log_level)

    def open(self, path=None):
        if path is None:
            path = self.PATH
        self.browser.get(self.browser.url + path)
        # self.logger.info(f"Opening url: {self.browser.url + path}")
        self.browser.logger.info(f"Opening url: {self.browser.url + path}")
        return self

    def get_title(self):
        # self.logger.info(f"Return title: '{self.browser.title}'")
        self.browser.logger.info(f"Return title: '{self.browser.title}'")
        return self.browser.title

    def alert(self):
        self.browser.logger.info(f"Check Alert of element '{self.ALERT}' is visibility")
        return WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.ALERT)).text

    def element(self, locator):
        # self.logger.info(f"Check if element '{locator}' is visibility")
        self.browser.logger.info(f"Check if element '{locator}' is visibility")
        return WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(locator))

    def elements(self, locator):
        # self.logger.info(f"Check if elements '{locator}' is visibility")
        self.browser.logger.info(f"Check if elements '{locator}' is visibility")
        return WebDriverWait(self.browser, 2).until(EC.visibility_of_all_elements_located(locator))

    def _input(self, element, value):
        # self.logger.info(f"Input '{value}' in '{element}'")
        self.browser.logger.info(f"Input '{value}' in element")
        element.clear()
        element.send_keys(value)
