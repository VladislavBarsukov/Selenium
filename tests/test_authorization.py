from pages.main_page import MainPage
from pages.authorization_page import Authorization
import pytest


def test_negative_authorization(driver):
    russian_error_text = "Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова."
    english_error_text = "Please check your password and account name and try again."
    main_page = MainPage()
    assert main_page.is_opened(), "Элемент при первом открытии страницы не отображается"
    main_page.go_to_login_page()
    Authorization().check_negative_authorization()
    neg_auth_error_text = Authorization().get_error_text()
    assert (russian_error_text in neg_auth_error_text) or (
                english_error_text in neg_auth_error_text), f"Ожидалось: {error_text}\n"f"Получено: {neg_auth_error_text}"
