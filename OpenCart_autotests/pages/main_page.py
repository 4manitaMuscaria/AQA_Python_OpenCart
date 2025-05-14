import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from OpenCart_autotests.pages.base_page import BasePage
from OpenCart_autotests.locators.main_page_locators import MainPageLocators


class MainPage(BasePage, MainPageLocators):

    @allure.step("Вызываем выпадающий список Desktops")
    def click_desktops(self):
        self.click(self.desktops_link)
        dropdown = self.get_element(self.desktops_dropdown)
        return dropdown.get_attribute("data-bs-popper")

    @allure.step("Переходим в раздел Desktops")
    def click_all_desktops(self):
        self.click(self.all_desktops_link)
        return self

    @allure.step("Вызываем выпадающий список My Account")
    def click_my_account(self):
        self.click(self.my_account)
        is_expanded = self.get_element(self.my_account)
        return is_expanded.get_attribute("aria-expanded")

    @allure.step("Перейти на форму регистрации")
    def open_register_account(self):
        self.click(self.register)
        return self

    @allure.step("Перейти к регистрации")
    def go_to_register(self):
        self.click((By.XPATH, self._text_xpath("span", "My Account")))
        self.click((By.XPATH, self._text_xpath("a", "Register")))


