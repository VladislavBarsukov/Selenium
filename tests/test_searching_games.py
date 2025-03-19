from pages.main_page import MainPage
from pages.search_games_page import SearchingGamesPage
import pytest


@pytest.mark.parametrize("game,n", (("The Witcher", 10), ("Fallout", 20)))
def test_searching_game(driver, game, n):
    base_page = MainPage()
    base_page.search_game_page(game)
    test_search_games = SearchingGamesPage()
    price_games = test_search_games.sort_games_from_high_to_low_price(n)
    sorted_price_games = sorted(price_games, reverse=True)
    assert sorted_price_games == price_games, "Сортировка по убыванию цены не работает"
