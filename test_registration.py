from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistration:
    CHROME_OPTIONS = Options()
    #CHROME_OPTIONS.add_argument("--no-sandbox")
    #CHROME_OPTIONS.add_argument('--headless=new')
    DRIVER = webdriver.Chrome(options=CHROME_OPTIONS)
    BASE_URL = 'https://store.steampowered.com/'

    def test_base_registration(self, driver=DRIVER, base_url=BASE_URL):
        driver.get(base_url)
        enter_element = driver.find_element(By.XPATH, '//*[@class="global_action_link"]')
        enter_element.click()
        login = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@type="text"]')))
        login.send_keys("a")
        password = driver.find_element(By.XPATH, '//*[@type="password"]')
        password.send_keys("b")
        enter = driver.find_element(By.XPATH, '//*[@type="submit"]')
        enter.click()
        #error_text = driver.find_element(By.XPATH,'//*[text()="Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова."]')
        #assert "Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова." == error_text.text
        driver.quit()