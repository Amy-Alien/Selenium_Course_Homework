from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(
        By.CSS_SELECTOR, "[name='firstname']").send_keys("Ivan")
    browser.find_element(
        By.CSS_SELECTOR, "[name='lastname']").send_keys("Ivanov")
    browser.find_element(By.CSS_SELECTOR, "[name='email']").send_keys(
        "emailivanova@mail.ru")

    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
# добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'text.txt')

    element = browser.find_element(By.ID, "file")
    element.send_keys(file_path)

    btn = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

finally:
    sleep(4)
    browser.quit()
