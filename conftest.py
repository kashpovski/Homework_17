import pytest
import logging
import datetime

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Browser to run tests")
    parser.addoption("--headless", action="store_true", help="Browser in headless mode")
    parser.addoption("--driver", default="D:\Mars\QA\WebDrivers", help="Directory to the webdriver")
    parser.addoption("--url", action="store_true", default="http://172.20.37.83:8081/", help="Base url")
    parser.addoption("--fullscreen", action="store_true", help="Open browser in full-screen mode")
    parser.addoption("--log_level", default="DEBUG", help="Set log level")


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    driver = request.config.getoption("--driver")
    url = request.config.getoption("--url")
    fullscreen = request.config.getoption("--fullscreen")
    log_level = request.config.getoption("--log_level")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.function.__name__}.log")
    file_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s %(funcName)s [%(module)s] | %(levelname)s :  %(message)s"))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    start_time = datetime.datetime.now()
    logger.info(f"===> Test started ===>")

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
    _browser.test_file = request.function.__name__
    _browser.test_name = request.node.name
    _browser.log_level = log_level
    _browser.logger = logger

    logger.info(f"Browser: {browser_name} ({_browser.session_id})")

    def fin():
        _browser.quit()
        logger.info(f"<=== Test finished. {datetime.datetime.now() - start_time} <===")

    request.addfinalizer(fin)

    return _browser

    # yield _browser
    #
    # logger.info(f"===/// Test finished. {datetime.datetime.now() - start_time}")
    #
    # _browser.quit()
