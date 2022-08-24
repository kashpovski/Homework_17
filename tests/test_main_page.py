import time

import pytest

from locators import MainPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_title(browser):
    browser.get(browser.url)
    assert browser.title == "Your Store"


def test_search_field(browser):
    browser.get(browser.url)
    wait = WebDriverWait(browser, 2)
    browser.find_element(*MainPage.SEARCH).send_keys("Mac")
    browser.find_element(*MainPage.BUTTON_SEARCH).click()
    wait.until(EC.presence_of_element_located(MainPage.SEARCH_FIELD))


@pytest.mark.parametrize("result", [("Desktops", "Laptops & Notebooks", "Components", "Tablets", "Software",
                                     "Phones & PDAs", "Cameras", "MP3 Players")], ids=["name elements in navbar"])
def test_nav_bar(browser, result):
    browser.get(browser.url)
    elements = browser.find_elements(*MainPage.NAVBAR)
    for el in elements:
        assert el.text in result, f"Not found element - '{el.text}' in Nav Bar"


@pytest.mark.parametrize("locator, currency", [(MainPage.EUR, "€"),
                                               (MainPage.GBP, "£"),
                                               (MainPage.USD, "$")], ids=["EUR", "GBP", "USD"])
def test_currency(browser, locator, currency):
    browser.get(browser.url)
    wait = WebDriverWait(browser, 2)
    browser.find_element(*MainPage.CHANGE_CURRENCY).click()
    wait.until(EC.element_to_be_clickable(locator)).click()
    time.sleep(1)
    assert len(browser.find_elements(By.XPATH, f"//*[contains(text(), '{currency}')]")) != 0
