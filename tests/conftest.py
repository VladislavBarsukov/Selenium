import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def driver():
    BASE_URL = "https://store.steampowered.com/"
    options = Options()
    # options.add_argument("--no-sandbox")
    # options.add_argument('--headless=new')
    driver = webdriver.Chrome(options=options)
    driver.get(BASE_URL)
    yield driver
    driver.quit()
