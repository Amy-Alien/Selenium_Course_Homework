import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(num):
    return str(math.log(abs(12*math.sin(int(num)))))


try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    input_checkbox = browser.find_element(By.ID, "robotCheckbox")
    input_checkbox.click()

    input_radiobutton = browser.find_element(By.ID, "robotsRule")
    input_radiobutton.click()

    submit_button = browser.find_element(
        By.CSS_SELECTOR, ".btn[type='submit']")
    submit_button.click()

finally:
    time.sleep(5)
    browser.quit()
