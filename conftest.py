from enum import Enum
import pytest
from selenium.webdriver.chrome.options import Options
from config.ConfigReader import ConfigReader
from WebDriver import WebDriver


class Language(Enum):
    RUSSIAN = 'ru,ru-RU'
    ENGLISH = 'en,en_US'


@pytest.fixture(scope='function')
def driver():
    BASE_URL = ConfigReader().get_value("url", "BASE_URL")
    options = Options()
    options.add_experimental_option('prefs', {
        'intl.accept_languages': Language.RUSSIAN.value
    })
    driver_instance = WebDriver(options=options)
    driver_instance.get_driver().get(BASE_URL)
    yield driver_instance
    WebDriver().quit()
