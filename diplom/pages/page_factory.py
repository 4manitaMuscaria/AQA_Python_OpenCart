from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageFactory:
    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger
        self.class_name = type(self).__name__
        self._initialize_elements()

    def _initialize_elements(self):
        # Инициализируем все элементы страницы
        for attr_name, attr_value in self.__class__.__dict__.items():
            if isinstance(attr_value, tuple) and len(attr_value) == 2:
                by, locator = attr_value
                setattr(self, attr_name, self._find_element(by, locator))

    def _find_element(self, by: str, locator: str) -> WebElement:
        return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((by, locator)))
