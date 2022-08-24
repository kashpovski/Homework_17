import random
import time

import pytest

from locators import ProdCardPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize("add_url, url_title", [("iphone", "iPhone"), ("imac", "iMac"), ("macbook", "MacBook")])
def test_title(browser, add_url, url_title):
    browser.get(browser.url + add_url)
    assert browser.title == url_title


@pytest.mark.parametrize("amount", ["1", "5", "33"])
@pytest.mark.parametrize("add_url", ["iphone", "imac", "macbook"])
def test_add_to_cart(browser, add_url, amount):
    browser.get(browser.url + add_url)
    browser.find_element(*ProdCardPage.QUANTITY).clear()
    browser.find_element(*ProdCardPage.QUANTITY).send_keys(amount)
    browser.find_element(*ProdCardPage.BUTTON_ADDTOCART).click()
    time.sleep(1)
    assert browser.find_element(*ProdCardPage.CART_TOTAL).text.split()[0] == amount


@pytest.mark.parametrize("add_url", ["iphone", "imac", "macbook"])
def test_reviews(browser, add_url):
    browser.get(browser.url + add_url)
    wait = WebDriverWait(browser, 2)
    browser.find_element(*ProdCardPage.REVIEWS).click()
    browser.find_element(*ProdCardPage.REVIEW_NAME).send_keys("user")
    browser.find_element(*ProdCardPage.REVIEW_TEXT).send_keys("This product very very very gooood!!!")
    browser.find_elements(*ProdCardPage.RATING)[random.randint(0, 4)].click()
    browser.find_element(*ProdCardPage.BUTTON_CONTINUE).click()
    assert wait.until(EC.presence_of_element_located(ProdCardPage.ALERT_SUCCESS))
