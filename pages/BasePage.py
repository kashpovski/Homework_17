from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    PATH = ""
    ALERT = (By.CSS_SELECTOR, "div.alert")

    def __init__(self, browser):
        self.browser = browser

    def open(self, path=None):
        if path is None:
            path = self.PATH
        self.browser.get(self.browser.url + path)
        return self

    def get_title(self):
        return self.browser.title

    def alert(self):
        return WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.ALERT)).text

    def element(self, locator):
        return WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(locator))

    def elements(self, locator):
        return WebDriverWait(self.browser, 2).until(EC.visibility_of_all_elements_located(locator))

    def _input(self, element, value):
        element.clear()
        element.send_keys(value)
