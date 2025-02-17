import time

import pytest
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from base_page import BasePage


class TestSearchingGames:
    TIME_OUT = 15
    SEARCH_ELEMENT = (By.ID, "store_nav_search_term")
    BUTTON_SEARCH = (By.XPATH, '//*[@id="store_search_link"]/img')
    SEARCHING_TYPE = (By.ID, "sort_by_trigger")
    SEARCHING_PRICE_DESC = (By.ID, "Price_DESC")
    SEARCH_RESULT_CONTAINER = (By.ID, "search_results")
    SORT_BY_TRIGGER = (By.XPATH, '//*[contains(@id, "sort_by") and contains(@value, "Price_DESC")]')
    GAME_PRICE = (By.XPATH, '//*[contains(@class, "col") and contains(@class, "search_price_discount_combined") and contains(@class, "responsive_secondrow")]')
    GAME_NAME = (By.XPATH, '//*[contains(@class, "col") and contains(@class, "search_name") and contains(@class, "ellipsis")]//*[contains(@class, "title")]')


    @pytest.mark.parametrize("game", {"The Witcher": 10, "Fallout": 20}.items())
    #@pytest.mark.parametrize("language", ["english", "russian"])
    def test_search_game(self, driver, game, language="russian"):
        pars_games_prises = {}
        BasePage(driver).switch_language(driver, language)
        BasePage(driver).search_game_page(game[0])
        button_search = WebDriverWait(driver, self.TIME_OUT).until(EC.element_to_be_clickable(self.BUTTON_SEARCH))
        button_search.click()
        searching_type_button = WebDriverWait(driver, self.TIME_OUT).until(
            EC.element_to_be_clickable(self.SEARCHING_TYPE))
        searching_type_button.click()
        searching_price_desc = WebDriverWait(driver, self.TIME_OUT).until(
            EC.element_to_be_clickable(self.SEARCHING_PRICE_DESC))
        searching_price_desc.click()

        first_search = WebDriverWait(driver, self.TIME_OUT).until(
            EC.visibility_of_element_located(self.SEARCH_RESULT_CONTAINER)).text
        WebDriverWait(driver, self.TIME_OUT).until(EC.presence_of_element_located(self.SORT_BY_TRIGGER))
        second_search = first_search
        while first_search == second_search:
            second_search = WebDriverWait(driver, self.TIME_OUT).until(
                EC.visibility_of_element_located(self.SEARCH_RESULT_CONTAINER)).text

        game_name = WebDriverWait(driver, self.TIME_OUT).until(EC.presence_of_all_elements_located(self.GAME_NAME))
        game_price = WebDriverWait(driver, self.TIME_OUT).until(EC.presence_of_all_elements_located(self.GAME_PRICE))

        for i in range(0, game[1]):
            #GAME_NAME = (By.XPATH, f'//*[@id="search_resultsRows"]//a[{i}]//span[1]')
            #game_name = WebDriverWait(driver, self.TIME_OUT).until(EC.visibility_of_element_located(self.GAME_NAME))
            #game_price = WebDriverWait(driver, self.TIME_OUT).until(EC.visibility_of_element_located(self.GAME_PRICE))
            pars_games = {game_name[i].text: game_price[i].text}
            pars_games_prises.update(pars_games)


        print(pars_games_prises)
        time.sleep(3)
