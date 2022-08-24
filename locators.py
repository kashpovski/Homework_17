from selenium.webdriver.common.by import By


class MainPage:
    SEARCH = (By.CSS_SELECTOR, "input[name = 'search']")
    BUTTON_SEARCH = (By.CSS_SELECTOR, "button.btn.btn-default.btn-lg")
    SEARCH_FIELD = (By.CSS_SELECTOR, "div#product-search")
    NAVBAR = (By.CSS_SELECTOR, "ul.nav.navbar-nav > li > a")
    SWIPER_ELEMENT = (By.CSS_SELECTOR, "div[class*='sw']:last-of-type > a[href] ")
    CHANGE_CURRENCY = (By.CSS_SELECTOR, "#form-currency [data-toggle]")
    EUR = (By.CSS_SELECTOR, "[name = 'EUR']")
    GBP = (By.CSS_SELECTOR, "[name = 'GBP']")
    USD = (By.CSS_SELECTOR, "[name = 'USD']")


class AdminLoginPage:
    USERNAME = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD = (By.CSS_SELECTOR, "input[name='password']")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "button[type='submit']")
    USER_MENU = (By.CSS_SELECTOR, "li.dropdown")
    HELP_BLOCK = (By.CSS_SELECTOR, ".help-block a")
    EMAIL = (By.CSS_SELECTOR, "input[name='email']")
    ALERT = (By.CSS_SELECTOR, "div.alert.alert-danger.alert-dismissible")


class RegUserPage:
    FIRSTNAME = (By.CSS_SELECTOR, "input[name='firstname']")
    LASTNAME = (By.CSS_SELECTOR, "input[name='lastname']")
    EMAIL = (By.CSS_SELECTOR, "input[name='email']")
    TELEPHONE = (By.CSS_SELECTOR, "input[name='telephone']")
    PASSWORD = (By.CSS_SELECTOR, "input[name='password']")
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, "input[name='confirm']")
    BUTTON_CONTINUE = (By.CSS_SELECTOR, "input[value='Continue']")
    CHECKBOX_PRIVACY_POLICY = (By.CSS_SELECTOR, "input[name='agree']")
    BUTTON_PRIVACY_POLICY = (By.CSS_SELECTOR, "a.agree")
    PRIVACY_POLICY = (By.CSS_SELECTOR, "div.modal-content")
    TEXT_DANGER = (By.CSS_SELECTOR, " ~ div")
    ACCOUNT_CREATED = (By.CSS_SELECTOR, "div#content>h1")


class ProdCardPage:
    CART_TOTAL = (By.CSS_SELECTOR, "span#cart-total")
    BUTTON_ADDTOCART = (By.CSS_SELECTOR, "button#button-cart")
    QUANTITY = (By.CSS_SELECTOR, "#input-quantity")
    REVIEWS = (By.CSS_SELECTOR, "[href='#tab-review']")
    REVIEW_NAME = (By.CSS_SELECTOR, "#input-name")
    REVIEW_TEXT = (By.CSS_SELECTOR, "#input-review")
    RATING = (By.CSS_SELECTOR, "[name='rating']")
    BUTTON_CONTINUE = (By.CSS_SELECTOR, "button#button-review")
    ALERT_SUCCESS = (By.CSS_SELECTOR, ".alert-success")


class CatPage:
    BUTTON_HOME = (By.CSS_SELECTOR, ".breadcrumb li:first-child a")
    BUTTON_LAPTOPS = (By.XPATH, "//*[@id='column-left']/*/*[contains(text(), 'Laptops & Notebooks')]")
    BUTTON_CAMERAS = (By.XPATH, "//*[@id='column-left']/*/*[contains(text(), 'Cameras')]")
    BUTTON_MP3 = (By.XPATH, "//*[@id='column-left']/*/*[contains(text(), 'MP3 Players')]")
    BUTTON_LIST = (By.CSS_SELECTOR, "#list-view")
    BUTTON_GRID = (By.CSS_SELECTOR, "#grid-view")
    PRODUCT = (By.CSS_SELECTOR, ".row .product-layout")
    COUNT_TEXT = (By.CSS_SELECTOR, ".text-right")


