from enum import StrEnum
import pytest
from selenium.webdriver.chrome.options import Options
from config.ConfigReader import ConfigReader
from CustomWebDriver import CustomWebDriver


class Language(StrEnum):
    RUSSIAN = 'ru-RU'
    ENGLISH = 'en-US'


@pytest.fixture(scope='function')
def driver():
    BASE_URL = ConfigReader().get_value("url", "BASE_URL")
    options = Options()
    options.add_argument(f"--lang={Language.ENGLISH}")
    driver_instance = CustomWebDriver(options=options)
    driver_instance.get_driver().get(BASE_URL)
    yield driver_instance
    driver_instance.quit()
