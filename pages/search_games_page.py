import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from WebDriver import WebDriver
import re
from config.ConfigReader import ConfigReader


class SearchingGamesPage:
    LOADING_OF_GAMES = (By.XPATH, '//*[contains(@style, "opacity: 0.5;") and contains(@id, "search_result_container")]')
    TIME_OUT = ConfigReader().get_value("time", "TIME_OUT")
    SEARCH_ELEMENT = (By.ID, "store_nav_search_term")
    SEARCHING_TYPE = (By.ID, "sort_by_trigger")
    SEARCHING_PRICE_DESC = (By.ID, "Price_DESC")
    SEARCH_RESULT_CONTAINER = (By.ID, "search_results")
    SORT_BY_TRIGGER = (By.XPATH, '//*[contains(@id, "sort_by") and contains(@value, "Price_DESC")]')
    GAME_PRICE = (By.XPATH,
                  '//*[contains(@class, "discount_final_price")]')

    def __init__(self):
        self.driver = WebDriver().get_driver()

    @staticmethod
    def get_prices(games):
        return [float(re.sub(r'[^\d,]', '', price).replace(',', '.')) for price in games]

    def sort_games_from_high_to_low_price(self, count):
        searching_type_button = WebDriverWait(self.driver, self.TIME_OUT).until(
            EC.element_to_be_clickable(self.SEARCHING_TYPE))
        searching_type_button.click()
        searching_price_desc = WebDriverWait(self.driver, self.TIME_OUT).until(
            EC.element_to_be_clickable(self.SEARCHING_PRICE_DESC))
        searching_price_desc.click()
        wait = WebDriverWait(self.driver, self.TIME_OUT, poll_frequency=0.05)
        wait.until(EC.presence_of_element_located(self.LOADING_OF_GAMES))
        wait.until(EC.invisibility_of_element_located(self.LOADING_OF_GAMES))
        game_price = WebDriverWait(self.driver, self.TIME_OUT).until(
            EC.presence_of_all_elements_located(self.GAME_PRICE))[:count]
        game_price = self.get_prices([i.text for i in game_price])
        return game_price
