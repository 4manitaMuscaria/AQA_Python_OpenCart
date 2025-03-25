import allure

from selenium.webdriver.common.by import By
from diplom.pages.base_page import BasePage


class LoginAdmin(BasePage):
    USERNAME = (By.XPATH, "//input[@id='input-username']")
    PASSWORD = (By.XPATH, "//input[@id='input-password']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()=' Login']")

    def __init__(self, browser):
        browser.get(f"{browser.url}/administration")
        super().__init__(browser)

    @allure.step("Ввести логин")
    def login_input(self, login):
        self.input_value(self.USERNAME, login)
        return self

    @allure.step("Ввести пароль")
    def password_input(self, password):
        self.input_value(self.PASSWORD, password)
        return self

    @allure.step("Кликнуть по кнопке Логин")
    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)
        return self

