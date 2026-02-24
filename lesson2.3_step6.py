from selenium import webdriver
from selenium.webdriver.common.by import By


from time import sleep
from math import log, sin

link = "http://suninjuly.github.io/redirect_accept.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    btn1 = browser.find_element(By.CSS_SELECTOR, ".trollface.btn.btn-primary")
    btn1.click()

    new_window = browser.window_handles[-1]
    browser.switch_to.window(new_window)
    sleep(1)

    x = browser.find_element(By.ID, "input_value").text
    answer = str(log(abs(12*sin(int(x)))))

    answer_form = browser.find_element(By.ID, "answer")
    answer_form.send_keys(answer)

    btn2 = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    btn2.click()

    output = browser.switch_to.alert.text
    output = output.split(": ")[-1]
    browser.switch_to.alert.accept()

    print(output)
finally:
    sleep(2)
    browser.quit()
