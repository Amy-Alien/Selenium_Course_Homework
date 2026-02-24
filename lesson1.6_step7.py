from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements(
        By.CSS_SELECTOR, ".first_block [type='text']")

    for el in elements:
        el.send_keys("1")

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()
finally:
    time.sleep(5)
    browser.quit()
