import pytest
import time
from selenium import webdriver



def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="Choose browser: chrome or firefox")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser_name")

    if browser_name == "chrome":
        print("\n---start Chrome browser for test---")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\n---start Firefox browser for test---")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("Please choose chrome or firefox in --browser_name")
    yield browser
    print("\n---quit browser---")
    time.sleep(2)
    browser.quit()

