from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from faker import Faker
from base_page import BasePage


class TestAuthorization:
    fake = Faker()
    TIME_OUT = 15
    LOGIN = (By.XPATH, '//*[@type="text"]')
    PASSWORD = (By.XPATH, '//*[@type="password"]')
    ENTER = (By.XPATH, '//*[@type="submit"]')
    ERROR_TEXT_ELEMENT = (By.XPATH, '//*[@class="page_content"]//div[5]')
    ERROR_TEXT = "Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова."

    def test_negative_authorization(self, driver):
        BasePage(driver).login_page()
        login = WebDriverWait(driver, self.TIME_OUT).until(EC.visibility_of_element_located(self.LOGIN))
        login.send_keys(self.fake.user_name())
        password = WebDriverWait(driver, self.TIME_OUT).until(EC.visibility_of_element_located(self.PASSWORD))
        password.send_keys(self.fake.password())
        enter = WebDriverWait(driver, self.TIME_OUT).until(EC.element_to_be_clickable(self.ENTER))
        enter.click()
        WebDriverWait(driver, self.TIME_OUT).until(lambda driver: WebDriverWait(driver, self.TIME_OUT).until(
            EC.presence_of_element_located(self.ERROR_TEXT_ELEMENT)).text.strip() != "")
        error_text_element = WebDriverWait(driver, self.TIME_OUT).until(
            EC.presence_of_element_located(self.ERROR_TEXT_ELEMENT))
        error_text = error_text_element.text
        assert self.ERROR_TEXT == error_text, f"Ожидалось: {self.ERROR_TEXT}\n"f"Получено: {error_text}"
