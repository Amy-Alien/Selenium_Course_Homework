from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

link = "http://suninjuly.github.io/selects.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text

    sum = str(int(num1) + int(num2))
    print(sum)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum)

    browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()
finally:
    sleep(4)
    browser.quit()
