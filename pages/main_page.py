from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from faker import Faker
from config.ConfigReader import ConfigReader
from WebDriver import WebDriver


class MainPage:
    TIME_OUT = ConfigReader().get_value("time", "TIME_OUT")
    FIRST_OPEN_SITE_ELEMENT = (
        By.XPATH, '//*[contains(@class, "store_nav")]')
    ENTRY_ELEMENT = (By.XPATH, '//*[contains(@class, "global_action_link")]')
    SEARCH_ELEMENT = (By.ID, "store_nav_search_term")
    LANGUAGE_LIST = (By.ID, 'language_pulldown')
    ENGLISH_LANGUAGE = (By.XPATH, "//*[contains(text(), 'English')]")
    RUSSIAN_LANGUAGE = (By.XPATH, "//*[contains(text(), 'Russian')]")
    CHANGE_LANGUAGE_ELEMENT = (
        By.XPATH, '//*[contains(@class, "waiting_dialog_container") and contains(@class, "waiting_dialog_centered")]')
    BUTTON_SEARCH = (By.XPATH, '//*[@id="store_search_link"]/img')
    fake = Faker()

    def __init__(self):
        self.driver = WebDriver().get_driver()

    def is_opened(self):
        is_opened = True
        try:
            WebDriverWait(self.driver, self.TIME_OUT).until(
                EC.visibility_of_element_located(self.FIRST_OPEN_SITE_ELEMENT))
        except TimeoutException:
            is_opened = False
        return is_opened

    def go_to_login_page(self):
        enter_element = WebDriverWait(self.driver, self.TIME_OUT).until(
            EC.element_to_be_clickable(self.ENTRY_ELEMENT))
        enter_element.click()

    def search_game_page(self, game):
        search_element = WebDriverWait(self.driver, self.TIME_OUT).until(
            EC.visibility_of_element_located(self.SEARCH_ELEMENT))
        search_element.send_keys(game)
        button_search = WebDriverWait(self.driver, self.TIME_OUT).until(EC.element_to_be_clickable(self.BUTTON_SEARCH))
        button_search.click()
