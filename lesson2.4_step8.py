from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from math import log, sin

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    btn1 = browser.find_element(By.ID, "book")

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    btn1.click()

    x = browser.find_element(By.ID, "input_value").text
    answer = str(log(abs(12*sin(int(x)))))

    answer_form = browser.find_element(By.ID, "answer")
    answer_form.send_keys(answer)

    btn2 = browser.find_element(By.ID, "solve")
    btn2.click()

    answer = browser.switch_to.alert.text
    answer = answer.split(": ")[-1]
    browser.switch_to.alert.accept()

    print(answer)
finally:
    browser.quit()
