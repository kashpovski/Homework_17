import pytest

from locators import CatPage


def test_back_home(browser):
    browser.get(browser.url + "desktops")
    browser.find_element(*CatPage.BUTTON_HOME).click()
    assert browser.title == "Your Store"


@pytest.mark.parametrize("locator, url_title", [(CatPage.BUTTON_LAPTOPS, "Laptops & Notebooks"),
                                                (CatPage.BUTTON_CAMERAS, "Cameras"),
                                                (CatPage.BUTTON_MP3, "MP3 Players")],
                         ids=["Laptops & Notebooks", "Cameras", "MP3 Players"])
def test_title(browser, locator, url_title):
    browser.get(browser.url + "desktops")
    browser.find_element(*locator).click()
    assert browser.title == url_title


@pytest.mark.parametrize("locator, class_name", [(CatPage.BUTTON_LIST,
                                                  "product-layout product-list col-xs-12"),
                                                 (CatPage.BUTTON_GRID,
                                                  "product-layout product-grid col-lg-4 col-md-4 col-sm-6 col-xs-12")],
                         ids=["LIST", "GRID"])
def test_view(browser, locator, class_name):
    browser.get(browser.url + "desktops")
    browser.find_element(*locator).click()
    prod = browser.find_elements(*CatPage.PRODUCT)
    for i in prod:
        assert i.get_attribute("class") == class_name


@pytest.mark.parametrize("locator", [CatPage.BUTTON_LAPTOPS, CatPage.BUTTON_CAMERAS, CatPage.BUTTON_MP3],
                         ids=["Laptops & Notebooks", "Cameras", "MP3 Players"])
def test_per_product_on_page(browser, locator):
    browser.get(browser.url + "desktops")
    browser.find_element(*locator).click()
    prod = browser.find_elements(*CatPage.PRODUCT)
    count = int(browser.find_element(*CatPage.COUNT_TEXT).text.split()[5])
    assert len(prod) == count


