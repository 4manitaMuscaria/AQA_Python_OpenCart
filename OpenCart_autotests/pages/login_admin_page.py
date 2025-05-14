import allure

from selenium.webdriver.common.by import By
from OpenCart_autotests.pages.base_page import BasePage
from OpenCart_autotests.locators.login_admin_locators import LoginAdminLocators


class LoginAdmin(BasePage, LoginAdminLocators):

    def __init__(self, browser):
        browser.get(f"{browser.url}/administration")
        super().__init__(browser)

    @allure.step("Ввести логин")
    def login_input(self, login):
        self.input_value(self.username, login)
        return self

    @allure.step("Ввести пароль")
    def password_input(self, password):
        self.input_value(self.password, password)
        return self

    @allure.step("Кликнуть по кнопке Логин")
    def click_login_button(self):
        self.click(self.login_button)
        return self

