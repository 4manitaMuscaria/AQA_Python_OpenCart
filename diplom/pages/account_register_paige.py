import allure

from selenium.common.exceptions import TimeoutException
from diplom.pages.base_page import BasePage
from diplom.locators.account_register_locators import AccountRegisterLocators


class AccountRegister(BasePage, AccountRegisterLocators):

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("Получить заголовок страницы")
    def get_title(self):
        try:
            self.get_element(self.title)
            return True
        except TimeoutException:
            return False

    @allure.step("Ввести имя")
    def input_first_name(self, username):
        self.input_value(self.first_name, username)
        first_name_value = self.get_element(self.first_name)
        return first_name_value.get_attribute("value")

    @allure.step("Ввести фамилию")
    def input_last_name(self, lastname):
        self.input_value(self.last_name, lastname)
        last_name_value = self.get_element(self.last_name)
        return last_name_value.get_attribute("value")

    @allure.step("Ввести e-mail")
    def input_email(self, email):
        self.input_value(self.email_element, email)
        last_name_value = self.get_element(self.email_element)
        return last_name_value.get_attribute("value")

    @allure.step("Ввести пароль")
    def input_password(self, password):
        self.input_value(self.password_element, password)
        last_name_value = self.get_element(self.password_element)
        return last_name_value.get_attribute("value")

    @allure.step("Переключить Privacy Policy")
    def click_privacy_policy_submit(self):
        self.click(self.privacy_policy)
        privacy_policy_submit = self.get_element(self.privacy_policy)
        return privacy_policy_submit.get_attribute("checked")

    @allure.step("Кликнуть по кнопке Continue")
    def click_continue_button(self):
        self.click(self.continue_button)
        return self

    @allure.step("Получить заголовлк страницы")
    def get_success_message(self):
        try:
            self.get_element(self.success_message)
            return True
        except TimeoutException:
            return False

    @allure.step("Кликнуть Continue")
    def click_continue_element(self):
        self.click(self.continue_element)
