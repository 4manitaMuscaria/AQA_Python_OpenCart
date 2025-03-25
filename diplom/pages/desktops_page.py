import allure

from selenium.common.exceptions import TimeoutException
from diplom.locators.desktops_locators import DesktopsLocators
from diplom.pages.base_page import BasePage


class Desktops(BasePage, DesktopsLocators):

    @allure.step("Находим заголовок страницы")
    def get_title(self):
        page_title = self.get_element(self.title)
        return page_title.text

    @allure.step("Кликаем на продукт")
    def go_to_product(self):
        self.click(self.product_link)
        try:
            self.click(self.product_link)
        except TimeoutException:
            pass
        return self
