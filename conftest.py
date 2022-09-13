import pytest

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="chrome", help="Browser to run tests"
    )
    parser.addoption(
        "--headless", action="store_true", help="Browser in headless mode"
    )
    parser.addoption(
        "--driver", action="store_true", default="D:\Mars\QA\WebDrivers", help="Directory to the webdriver"
    )
    parser.addoption(
        "--url", action="store_true", default="http://172.30.79.207:8081/", help="Base url"
    )
    parser.addoption(
        "--fullscreen", action="store_true", help="Open browser in full-screen mode"
    )


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    driver = request.config.getoption("--driver")
    url = request.config.getoption("--url")
    fullscreen = request.config.getoption("--fullscreen")

    options = webdriver.ChromeOptions()
    if headless:
        options.headless = True

    if browser_name == "chrome":
        _browser = webdriver.Chrome(executable_path=driver + "\chromedriver",
                                    options=options)
    elif browser_name == "firefox":
        _browser = webdriver.Firefox(executable_path=driver + "\geckodriver")
    elif browser_name == "opera":
        _browser = webdriver.Opera(executable_path=driver + "\operadriver")
    elif browser_name == "yandex":
        _browser = webdriver.Chrome(executable_path=driver + "\yandexdriver",
                                    options=options)
    elif browser_name == "edge":
        _browser = webdriver.Edge(executable_path=driver + "\msedgedriver")
    else:
        raise ValueError(f"Browser '{browser_name}' is not supported ")

    if fullscreen:
        _browser.maximize_window()

    _browser.url = url

    yield _browser

    _browser.quit()
