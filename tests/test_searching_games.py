from pages.main_page import MainPage
from pages.search_games_page import SearchingGames
import pytest


@pytest.mark.parametrize("game", {"The Witcher": 10, "Fallout": 20}.items())
def test_searching_game(driver, game):
    base_page = MainPage()
    base_page.search_game_page(game[0])
    test_search_games = SearchingGames()
    count_games = test_search_games.search_game(game[1])
    assert len(count_games) == game[1], "Количество игр не совпадает"
