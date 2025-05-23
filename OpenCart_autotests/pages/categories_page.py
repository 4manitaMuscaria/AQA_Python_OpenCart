import allure

from OpenCart_autotests.pages.base_page import BasePage
from OpenCart_autotests.locators.categories_locators import CategoriesLocators


class Categories(BasePage, CategoriesLocators):

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("Кликнуть по кнопке Add New")
    def add_new(self):
        self.click(self.add_new_button)
        return self
