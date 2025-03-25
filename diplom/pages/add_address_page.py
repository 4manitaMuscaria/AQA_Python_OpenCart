import allure

from selenium.common.exceptions import TimeoutException
from diplom.pages.base_page import BasePage
from diplom.locators.add_address_locators import AddAddressLocators


class AddAddress(BasePage, AddAddressLocators):

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("Получаем заголовок формы")
    def get_add_address_title(self):
        try:
            self.get_element(self.address_title)
            return True
        except TimeoutException:
            return False

    @allure.step("Вводим адрес")
    def address_input(self, address):
        self.input_value(self.address_1_input, address)
        address_value = self.get_element(self.address_1_input)
        return address_value.get_attribute("value")

    @allure.step("Выбираем страну")
    def select_country(self, country):
        self.select(self.country_select, country)
        country_val = self.get_element(self.country_select)
        return country_val.get_attribute("value")

    @allure.step("Устанавливаем необходимые значения")
    def set_address_form_values(self, firstname, lastname, address, city, country, zone):
        self.input_value(self.first_name, firstname)
        self.input_value(self.last_name, lastname)
        self.input_value(self.address_1_input, address)
        self.input_value(self.city_input, city)
        self.select(self.country_select, country)
        self.select(self.zone_select, zone)
        self.click(self.continue_button)
        try:
            self.get_elements(self.validation_error)
            return True
        except TimeoutException:
            return False
