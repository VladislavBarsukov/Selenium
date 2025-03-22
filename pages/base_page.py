from CustomWebDriver import CustomWebDriver

class BasePage:
    def __init__(self):
        self.driver = CustomWebDriver().get_driver()