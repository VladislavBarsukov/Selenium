from pages.main_page import MainPage
from pages.authorization_page import Authorization


def test_negative_authorization(driver):
    error_text = "Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова."
    base_page = MainPage()
    assert base_page.is_opened(), "Элемент при первом открытии страницы не отображается"
    base_page.go_to_login_page()
    Authorization().check_negative_authorization()
    neg_auth_error_text = Authorization().get_error_text()
    assert neg_auth_error_text == error_text, f"Ожидалось: {error_text}\n"f"Получено: {neg_auth_error_text}"
