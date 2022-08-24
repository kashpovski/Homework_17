import pytest

from locators import AdminLoginPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_title(browser):
    browser.get(browser.url + "admin")
    assert browser.title == "Administration"


def test_valid_login(browser, username, password):
    browser.get(browser.url + "admin")
    wait = WebDriverWait(browser, 2)
    browser.find_element(*AdminLoginPage.USERNAME).send_keys(username)
    browser.find_element(*AdminLoginPage.PASSWORD).send_keys(password)
    browser.find_element(*AdminLoginPage.BUTTON_LOGIN).click()
    wait.until(EC.presence_of_element_located(AdminLoginPage.USER_MENU))


@pytest.mark.parametrize("random_username_password", [("letters", 10)], ids=["letters"], indirect=True)
def test_invalid_login_attempts(browser, random_username_password):
    browser.get(browser.url + "admin")
    wait = WebDriverWait(browser, 2)
    browser.find_element(*AdminLoginPage.USERNAME).send_keys(random_username_password)
    browser.find_element(*AdminLoginPage.PASSWORD).send_keys("any_password")
    for i in range(6):
        browser.find_element(*AdminLoginPage.BUTTON_LOGIN).click()
    assert wait.until(EC.presence_of_element_located(AdminLoginPage.ALERT)).text == "Warning: Your account has " \
                                                                                    "exceeded allowed number of " \
                                                                                    "login attempts. Please try " \
                                                                                    "again in 1 hour or reset " \
                                                                                    "password.\n×"


@pytest.mark.parametrize("random_username_password", [("digits", 5),
                                             ("letters", 5),
                                             ("simbols", 5),
                                             ("", 5)], ids=["digits", "letters", "simbols", "Nothing"], indirect=True)
def test_invalid_login(browser, random_username_password):
    browser.get(browser.url + "admin")
    wait = WebDriverWait(browser, 2)
    browser.find_element(*AdminLoginPage.USERNAME).send_keys(random_username_password)
    browser.find_element(*AdminLoginPage.PASSWORD).send_keys(random_username_password)
    browser.find_element(*AdminLoginPage.BUTTON_LOGIN).click()
    assert wait.until(EC.presence_of_element_located(AdminLoginPage.ALERT)).text == "No match for Username and/or " \
                                                                                    "Password.\n×"


def test_forgotten_password(browser):
    browser.get(browser.url + "admin")
    wait = WebDriverWait(browser, 2)
    help_block = browser.find_element(*AdminLoginPage.HELP_BLOCK)
    assert help_block.text == "Forgotten Password"
    help_block.click()
    assert wait.until(EC.presence_of_element_located(AdminLoginPage.EMAIL))

