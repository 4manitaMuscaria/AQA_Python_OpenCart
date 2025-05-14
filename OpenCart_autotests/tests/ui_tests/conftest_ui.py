import pytest
import datetime
import allure
import json
from selenium import webdriver
from selenium.webdriver import FirefoxOptions, ChromeOptions, EdgeOptions
from OpenCart_autotests.config.credentials import Credetntials


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--maximize", action="store_true")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--url", action="store", default=f"http://{Credetntials.HOST}/", help="This is request url")
    parser.addoption("--execution", action="store", default="remote")
    parser.addoption("--executor", default="127.0.0.1")
    parser.addoption("--bv")
    parser.addoption("--video", action="store_false")


@pytest.fixture()
def browser(request, logger):
    """
    Запуск браузера
    """
    browser_name = request.config.getoption("--browser")
    browser_version = request.config.getoption("--bv")
    maximize = request.config.getoption("--maximize")
    headless = request.config.getoption("--headless")
    url = request.config.getoption("--url")
    executor = request.config.getoption("--executor")
    execution = request.config.getoption("--execution")
    video_enabled = request.config.getoption("--video")

    logger.info("===> Test %s started at %s" % (request.node.name, datetime.datetime.now()))

    if execution == "local":                # работаем локально
        if browser_name == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("headless=new")
            driver = webdriver.Chrome(options=options)
        elif browser_name == "firefox":
            options = FirefoxOptions()
            if headless:
                options.headless = True
            driver = webdriver.Firefox(options=options)
        elif browser_name == "edge":
            options = EdgeOptions()
            if headless:
                options.add_argument("headless=new")
            driver = webdriver.Edge(options=options)
        else:
            raise ValueError("Browser name should be one of 'chrome', 'firefox', 'edge'")

    elif execution == "remote":             # работаем удаленно

        caps = {
            "browserName": browser_name,
            "browserVersion": browser_version,
            "selenoid:options": {
                "enableVideo": video_enabled
            }
        }

        if browser_name == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("headless=new")
        elif browser_name == "firefox":
            options = FirefoxOptions()
            if headless:
                options.headless = True
        elif browser_name == "edge":
            options = EdgeOptions()
            if headless:
                options.add_argument("headless=new")
        else:
            raise ValueError("Browser name should be one of 'chrome', 'firefox', 'edge'")

        for (k, v) in caps.items():
            options.set_capability(k, v)
        driver = webdriver.Remote(
            command_executor=f'http://{executor}:4444/wd/hub',
            options=options
        )

    else:
        raise ValueError("Execution should be one of 'local' or 'remote'")

    allure.attach(
        name=driver.session_id,
        body=json.dumps(driver.capabilities, indent=4, ensure_ascii=False),
        attachment_type=allure.attachment_type.JSON)

    driver.logger = logger
    driver.is_headless = headless
    driver.test_name = request.node.name

    logger.info("Browser %s started" % browser)

    if maximize:
        driver.maximize_window()

    # request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    # return driver

    yield driver

    status = request.node.funcargs.get("test_status")
    if status == "failed":
        allure.attach(
            name="failure_screenshot",
            body=driver.get_screenshot_as_png(),
            attachment_type=allure.attachment_type.PNG
        )
        allure.attach(
            body=driver.page_source,
            name='Attach_with_HTML_type',
            attachment_type=allure.attachment_type.HTML
        )

    driver.quit()

    logger.info("===> Test %s finished at %s \n" % (request.node.name, datetime.datetime.now()))

