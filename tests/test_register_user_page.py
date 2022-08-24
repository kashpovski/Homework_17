import pytest

from locators import RegUserPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_title(browser):
    browser.get(browser.url + "index.php?route=account/register")
    assert browser.title == "Register Account"


def test_privacy_policy(browser):
    browser.get(browser.url + "index.php?route=account/register")
    wait = WebDriverWait(browser, 2)
    browser.find_element(*RegUserPage.BUTTON_PRIVACY_POLICY).click()
    wait.until(EC.presence_of_element_located(RegUserPage.PRIVACY_POLICY))


@pytest.mark.parametrize("locator, text_danger", [(RegUserPage.FIRSTNAME,
                                                   "First Name must be between 1 and 32 characters!"),
                                                  (RegUserPage.LASTNAME,
                                                   "Last Name must be between 1 and 32 characters!"),
                                                  (RegUserPage.EMAIL,
                                                   "E-Mail Address does not appear to be valid!"),
                                                  (RegUserPage.TELEPHONE,
                                                   "Telephone must be between 3 and 32 characters!"),
                                                  (RegUserPage.PASSWORD, "Password must be between 4 and 20 characters!")],
                         ids=["FIRSTNAME", "LASTNAME", "EMAIL", "TELEPHONE", "PASSWORD"])
def test_text_danger(browser, locator, text_danger):
    browser.get(browser.url + "index.php?route=account/register")
    wait = WebDriverWait(browser, 2)
    assert wait.until_not(EC.presence_of_element_located((locator[0], locator[1] + RegUserPage.TEXT_DANGER[1])))
    browser.find_element(*RegUserPage.BUTTON_CONTINUE).click()
    assert wait.until(EC.presence_of_element_located((locator[0], locator[1] + RegUserPage.TEXT_DANGER[1])))
    assert wait.until(EC.presence_of_element_located((locator[0], locator[1] + RegUserPage.TEXT_DANGER[1]))).text == \
           text_danger


@pytest.mark.parametrize("random_username_password", [("letters", 10)], ids=["registration"], indirect=True)
def test_success_account_created(browser, random_username_password):
    browser.get(browser.url + "index.php?route=account/register")
    wait = WebDriverWait(browser, 2)
    browser.find_element(*RegUserPage.FIRSTNAME).send_keys(random_username_password)
    browser.find_element(*RegUserPage.LASTNAME).send_keys(random_username_password)
    browser.find_element(*RegUserPage.EMAIL).send_keys(random_username_password + "@email.ru")
    browser.find_element(*RegUserPage.TELEPHONE).send_keys(98765432100)
    browser.find_element(*RegUserPage.PASSWORD).send_keys(random_username_password)
    browser.find_element(*RegUserPage.PASSWORD_CONFIRM).send_keys(random_username_password)
    browser.find_element(*RegUserPage.CHECKBOX_PRIVACY_POLICY).click()
    browser.find_element(*RegUserPage.BUTTON_CONTINUE).click()
    assert wait.until(EC.presence_of_element_located(RegUserPage.ACCOUNT_CREATED)).text == \
           "Your Account Has Been Created!"
