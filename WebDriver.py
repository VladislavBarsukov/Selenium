from selenium import webdriver


class WebDriver:
    _options = None
    _instance = None

    def __new__(cls, options=None):
        if cls._instance is None:
            cls._options = options
            cls._instance = super().__new__(cls)
            cls._instance.driver = webdriver.Chrome(options=cls._options)
        return cls._instance

    def get_driver(self):
        return self.driver

    def cleanup(self):
        WebDriver._instance = None
        _options = None
        self.driver.quit()
