import pytest
import logging
import datetime
import json

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from browsermobproxy import Server, Client


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Browser to run tests")
    parser.addoption("--headless", action="store_true", help="Browser in headless mode")
    parser.addoption("--driver", default="D:\Mars\QA\WebDrivers", help="Directory to the webdriver")
    parser.addoption("--url", action="store_true", default="http://172.20.43.209:8081/", help="Base url")
    parser.addoption("--fullscreen", action="store_true", help="Open browser in full-screen mode")
    parser.addoption("--log_level", default="DEBUG", help="Set log level")


@pytest.fixture
def proxy_server(request):
    server = Server(r"D:\Mars\QA\OTUS\lesson_17\Homework_17\browsermob-proxy-2.1.4\bin\browsermob-proxy.bat",
                    {"port": 8082})
    server.start({"log_path": "logs_proxy"})
    client = Client("localhost:8082")
    server.create_proxy()
    request.addfinalizer(server.stop)
    client.new_har() #Архив сетевой активнти браузера (список словарей)
    return client


@pytest.fixture
def browser(request, proxy_server):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    driver = request.config.getoption("--driver")
    url = request.config.getoption("--url")
    fullscreen = request.config.getoption("--fullscreen")
    log_level = request.config.getoption("--log_level")
    caps = DesiredCapabilities.CHROME

    caps['goog:loggingPrefs'] = {
        'browser': 'ALL',
        'performance': 'ALL',
    }

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

    options.accept_insecure_certs = True
    proxy_server.add_to_webdriver_capabilities(caps)

    if browser_name == "chrome":
        _browser = webdriver.Chrome(executable_path=driver + "\chromedriver",
                                    options=options,
                                    desired_capabilities=caps)
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
    _browser.proxy = proxy_server

    logger.info(f"Browser: {browser_name} ({_browser.session_id})")

    def dump_log_proxy_to_json(har_log, file_name):
        logs = []
        with open(file_name, "w+") as f:
            for i, el in enumerate(har_log["entries"], start=1):
                logs.append({i: {"request": el["request"], "response": el["response"]}})
            f.write(json.dumps(logs))

    def fin():

        # Логиирование производительности страницы
        performance_logs = []
        for line in _browser.get_log("performance"):
            performance_logs.append(line)
        with open(f"logs_browser/{request.function.__name__}_performance.json", "w+") as f:
            f.write(json.dumps(performance_logs))

        # Логи консоли браузера собирает WARNINGS, ERRORS
        browser_logs = []
        for line in _browser.get_log("browser"):
            browser_logs.append(line)
        with open(f"logs_browser/{request.function.__name__}_browser.json", "w+") as f:
            f.write(json.dumps(browser_logs))

        dump_log_proxy_to_json(_browser.proxy.har['log'], f"logs_proxy/{request.function.__name__}_proxy.json")

        _browser.proxy.close()
        _browser.quit()

        logger.info(f"<=== Test finished. {datetime.datetime.now() - start_time} <===")

    request.addfinalizer(fin)

    return _browser
