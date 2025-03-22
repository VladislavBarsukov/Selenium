from pages.main_page import MainPage
from pages.search_games_page import SearchingGamesPage
import pytest


@pytest.mark.parametrize("game,n", (("The Witcher", 10), ("Fallout", 20)))
def test_searching_game(driver, game, n):
    main_page = MainPage()
    main_page.search_game_page(game)
    test_search_games = SearchingGamesPage()
    test_search_games.sort_games_from_high_to_low_price()
    price_games = test_search_games.parsing_prices(n)
    sorted_price_games = sorted(price_games, reverse=True)
    assert sorted_price_games == price_games, f"Ожидалась последовательность цен {sorted_price_games}, получили {price_games}"
