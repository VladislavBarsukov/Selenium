from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from faker import Faker
from config.ConfigReader import ConfigReader
from pages.base_page import BasePage


class Authorization(BasePage):
    fake = Faker()
    a = ConfigReader()
    TIME_OUT = a.get_value("time", "TIME_OUT")
    LOGIN = (By.XPATH, '//*[@type="text"]')
    PASSWORD = (By.XPATH, '//*[@type="password"]')
    ENTER = (By.XPATH, '//*[@type="submit"]')
    ERROR_TEXT_ELEMENT = (By.XPATH, '//*[@class="page_content"]//div[5]')

    def __init__(self):
        super().__init__()

    def check_negative_authorization(self):
        login = WebDriverWait(self.driver, self.TIME_OUT).until(EC.visibility_of_element_located(self.LOGIN))
        login.send_keys(self.fake.user_name())
        password = WebDriverWait(self.driver, self.TIME_OUT).until(EC.visibility_of_element_located(self.PASSWORD))
        password.send_keys(self.fake.password())
        enter = WebDriverWait(self.driver, self.TIME_OUT).until(EC.element_to_be_clickable(self.ENTER))
        enter.click()

    def get_error_text(self):
        WebDriverWait(self.driver, self.TIME_OUT).until(lambda driver: WebDriverWait(self.driver, self.TIME_OUT).until(
            EC.presence_of_element_located(self.ERROR_TEXT_ELEMENT)).text.strip() != "")
        error_text_element = WebDriverWait(self.driver, self.TIME_OUT).until(
            EC.presence_of_element_located(self.ERROR_TEXT_ELEMENT))
        return error_text_element.text
