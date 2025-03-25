import allure

from diplom.pages.base_page import BasePage
from diplom.locators.iframe_locators import IframeLocators


class IframeElement(BasePage, IframeLocators):

    def __init__(self, browser):
        super().__init__(browser)
        self.iframe_element = self.get_element(self.iframe)

    @allure.step("Переключаемся в iframe и вводим текст описания")
    def input_description(self, description_val):
        with self.switch_to_frame(self.iframe):
            self.input_value(self.description, description_val)
            return self.get_element(self.description).text
