from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from WebDriver import WebDriver
from config.ConfigReader import ConfigReader


class SearchingGames:
    TIME_OUT = ConfigReader(config_file_path="config.json").get_value("time", "TIME_OUT")
    SEARCH_ELEMENT = (By.ID, "store_nav_search_term")
    SEARCHING_TYPE = (By.ID, "sort_by_trigger")
    SEARCHING_PRICE_DESC = (By.ID, "Price_DESC")
    SEARCH_RESULT_CONTAINER = (By.ID, "search_results")
    SORT_BY_TRIGGER = (By.XPATH, '//*[contains(@id, "sort_by") and contains(@value, "Price_DESC")]')
    GAME_PRICE = (By.XPATH,
                  '//*[contains(@class, "col") and contains(@class, "search_price_discount_combined") and contains(@class, "responsive_secondrow")]')
    GAME_NAME = (By.XPATH,
                 '//*[contains(@class, "col") and contains(@class, "search_name") and contains(@class, "ellipsis")]//*[contains(@class, "title")]')

    def __init__(self):
        self.driver = WebDriver().get_driver()

    def search_game(self, count):
        searching_type_button = WebDriverWait(self.driver, self.TIME_OUT).until(
            EC.element_to_be_clickable(self.SEARCHING_TYPE))
        searching_type_button.click()
        searching_price_desc = WebDriverWait(self.driver, self.TIME_OUT).until(
            EC.element_to_be_clickable(self.SEARCHING_PRICE_DESC))
        searching_price_desc.click()

        first_search = WebDriverWait(self.driver, self.TIME_OUT).until(
            EC.visibility_of_element_located(self.SEARCH_RESULT_CONTAINER)).text
        WebDriverWait(self.driver, self.TIME_OUT).until(EC.presence_of_element_located(self.SORT_BY_TRIGGER))
        second_search = first_search
        while first_search == second_search:
            second_search = WebDriverWait(self.driver, self.TIME_OUT).until(
                EC.visibility_of_element_located(self.SEARCH_RESULT_CONTAINER)).text

        game_name = WebDriverWait(self.driver, self.TIME_OUT).until(
            EC.presence_of_all_elements_located(self.GAME_NAME))[:count]
        game_name = [i.text for i in game_name]
        return game_name
