import pytest
import time
import math
from stepik_logpass import LOGIN, PASSWORD
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

final_answer = ""

# Create the fixture with print final answer in the end
@pytest.fixture(scope="function")
def browser():
    print("\n---start browser for test---")
    browser = webdriver.Chrome()
    yield browser
    print("\n---quit browser---")
    time.sleep(2)
    print(final_answer)
    browser.quit()

class Test_Stepik:
    id_lessons = ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905", ]

    @pytest.mark.smoke()
    def login(self, browser):
        WebDriverWait(browser, 20).until(EC.presence_of_element_located((
            By.CSS_SELECTOR, ".ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button"
        ))).click()

        browser.find_element(By.ID, "id_login_email").send_keys(LOGIN)
        browser.find_element(By.ID, "id_login_password").send_keys(PASSWORD)
        browser.find_element(By.CSS_SELECTOR, ".sign-form__btn.button_with-loader").click()

        WebDriverWait(browser,10).until(EC.invisibility_of_element_located((
            By.CSS_SELECTOR,".ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button"
        )))

    @pytest.mark.parametrize("id", id_lessons)
    def test_stepik_login(self, browser, id):
        browser.get(f"https://stepik.org/lesson/{id}/step/1")
        browser.implicitly_wait(10)
        Test_Stepik.login(self, browser)

        # CHECK ANSWER FORM AND CLEAN IT
        if len(browser.find_elements(By.CSS_SELECTOR, "button.again-btn")) > 0:
            browser.find_element(By.CSS_SELECTOR, "button.again-btn").click()
            if len(browser.find_elements(By.CSS_SELECTOR, "footer.modal-popup__footer button")) > 0:
                browser.find_element(By.CSS_SELECTOR, "footer.modal-popup__footer button").click()
                time.sleep(1)
            time.sleep(1)

        # SEND ANSWER
        form_for_answer = WebDriverWait(browser,10).until(EC.presence_of_element_located((
            By.CSS_SELECTOR, 'textarea.ember-text-area.ember-view.textarea.string-quiz__textarea'
        )))
        time.sleep(1)
        form_for_answer.clear()
        form_for_answer.send_keys(str(math.log(int(time.time()))))


        submit_button = WebDriverWait(browser,10).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "button.submit-submission"
        )))
        time.sleep(2)
        submit_button.click()

        # CHECK HINT
        hint = WebDriverWait(browser,20).until(EC.presence_of_element_located((
            By.CSS_SELECTOR,"p.smart-hints__hint"
        ))).text

        # SAVE HINT
        if "Correct!" not in hint:
            global final_answer
            final_answer += hint

        assert "Correct!" in hint, f"Hint of answer is not correct. Hint = {hint}"

if __name__ == "__main__":
    pytest.main()