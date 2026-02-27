import pytest
import time
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\n---start browser for test---")
    browser = webdriver.Chrome()
    yield browser
    print("\n---quit browser---")
    time.sleep(2)
    browser.quit()

