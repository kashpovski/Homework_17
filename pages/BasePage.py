from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    PATH = ""
    ALERT = (By.CSS_SELECTOR, "div.alert")

    def __init__(self, browser):
        self.browser = browser
        self.actions = ActionChains(browser)

    def open(self, path=None):
        if path is None:
            path = self.PATH
        self.browser.get(self.browser.url + path)
        # self.logger.info(f"Opening url: {self.browser.url + path}")
        # self.browser.logger.info(f"Opening url: {self.browser.url + path}")
        return self

    def get_title(self):
        # self.logger.info(f"Return title: '{self.browser.title}'")
        # self.browser.logger.info(f"Return title: '{self.browser.title}'")
        return self.browser.title

    def alert(self):
        # self.browser.logger.info(f"Check Alert of element '{self.ALERT}' is visibility")
        return WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.ALERT)).text

    def element(self, locator):
        # self.logger.info(f"Check if element '{locator}' is visibility")
        # self.browser.logger.info(f"Check if element '{locator}' is visibility")
        return WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(locator))

    def elements(self, locator):
        # self.logger.info(f"Check if elements '{locator}' is visibility")
        # self.browser.logger.info(f"Check if elements '{locator}' is visibility")
        return WebDriverWait(self.browser, 2).until(EC.visibility_of_all_elements_located(locator))

    def _input(self, element, value):
        # self.logger.info(f"Input '{value}' in '{element}'")
        # self.browser.logger.info(f"Input '{value}' in element")
        element.clear()
        element.send_keys(value)
