from selenium import webdriver


class CustomWebDriver:
    _driver = None

    def __new__(cls, options=None):
        if cls._driver is None:
            cls._driver = webdriver.Chrome(options=options)
        return cls

    @classmethod
    def get_driver(cls):
        return cls._driver

    @classmethod
    def quit(cls):
        if cls._driver:
            cls._driver.quit()
        cls._driver = None
