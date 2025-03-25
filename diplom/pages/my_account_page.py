import allure

from selenium.common.exceptions import TimeoutException
from diplom.pages.base_page import BasePage
from diplom.locators.my_account_locators import MyAccountLocators


class MyAccount(BasePage, MyAccountLocators):

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("Получить заголовок страницы")
    def get_my_account_title(self):
        try:
            self.get_element(self.account_title)
            return True
        except TimeoutException:
            return False

    @allure.step("Перейти к редактированию адресной книги")
    def open_address_book(self):
        self.click(self.address_book_link)
        return self

    @allure.step("Получить заголовок адресной книги")
    def get_address_book_title(self):
        try:
            self.get_element(self.address_book_title)
            return True
        except TimeoutException:
            return False

    @allure.step("Кликнуть New Address")
    def click_new_address(self):
        self.click(self.new_address_button)
        return self

    @allure.step("Найти адрес в адресной книге")
    def get_address(self):
        address = self.get_element(self.address_element)
        return address.text
