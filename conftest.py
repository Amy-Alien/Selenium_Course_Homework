import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\n---start browser for test---")
    browser = webdriver.Chrome()
    yield browser
    print("\n---quit browser---")
    browser.quit()
