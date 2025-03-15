from pages.main_page import MainPage
from pages.authorization_page import Authorization


def test_negative_authorization(driver):
    ERROR_TEXT = "Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова."
    base_page = MainPage()
    assert base_page.is_opened() == True, "Элемент при первом открытии страницы не отображается"
    base_page.login_page()
    error_text = Authorization().negative_authorization()
    assert error_text == ERROR_TEXT, f"Ожидалось: {ERROR_TEXT}\n"f"Получено: {error_text}"
