from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

link = "https://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "input_value").text
    y = str(math.log(abs(12*math.sin(int(x)))))

    print(y)
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    browser.execute_script("window.scrollBy(0, 100);")

    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()

    button.click()


finally:
    sleep(4)
    browser.quit()
