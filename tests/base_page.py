import time

import pytest
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from faker import Faker


class BasePage:
    TIME_OUT = 15
    FIRST_OPEN_SITE_ELEMENT = (
        By.XPATH, '//*[contains(@class, "home_page_content") and contains(@class, "special_offers")]')
    ENTRY_ELEMENT = (By.XPATH, '//*[contains(@class, "global_action_link")]')
    SEARCH_ELEMENT = (By.ID, "store_nav_search_term")
    LANGUAGE_LIST = (By.ID, 'language_pulldown')
    RUSSIAN_LANGUAGE = (By.XPATH, "//*[href='?l=english']")
    ENGLISH_LANGUAGE = (By.XPATH, "//*[contains(text(), 'English')]")
    CHANGE_ELEMENT = (By.XPATH, '//*[contains(@class, "waiting_dialog_container waiting_dialog_centered")]')

    def __init__(self, driver):
        self.driver = driver
        self.fake = Faker()
        self.base_opened()

    def switch_language(self, driver, language):
        if language == 'russian':
            return None
        language_list = WebDriverWait(driver, self.TIME_OUT).until(EC.element_to_be_clickable(self.LANGUAGE_LIST))
        language_list.click()
        change_language = WebDriverWait(driver, self.TIME_OUT).until(EC.element_to_be_clickable(self.ENGLISH_LANGUAGE))
        change_language.click()
        WebDriverWait(driver, self.TIME_OUT).until(EC.visibility_of_element_located(self.CHANGE_ELEMENT))
        WebDriverWait(driver, self.TIME_OUT).until_not(EC.visibility_of_element_located(self.CHANGE_ELEMENT))
        self.base_opened()

    def base_opened(self):
        is_opened = True
        try:
            WebDriverWait(self.driver, self.TIME_OUT).until(
                EC.visibility_of_element_located(self.FIRST_OPEN_SITE_ELEMENT))
        except TimeoutException:
            is_opened = False
        assert is_opened, "Элемент при первом открытии страницы не отображается"

    def login_page(self):
        enter_element = WebDriverWait(self.driver, self.TIME_OUT).until(
            EC.visibility_of_element_located(self.ENTRY_ELEMENT))
        enter_element.click()

    def search_game_page(self, game):
        search_element = WebDriverWait(self.driver, self.TIME_OUT).until(
            EC.visibility_of_element_located(self.SEARCH_ELEMENT))
        search_element.send_keys(game)
