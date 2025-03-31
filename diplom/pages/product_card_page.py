import time
import allure

from selenium.common.exceptions import TimeoutException
from diplom.pages.base_page import BasePage
from diplom.locators.product_card_locators import ProductCardLocators


class ProductCard(BasePage, ProductCardLocators):

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("Ожидать загрузки карточки товара")
    def waiting_for_product_card(self):
        name = self.get_element(self.product_name)
        return name.text

    @allure.step("Кликнуть Добавить в корзину")
    def click_add_to_cart(self):
        self.click(self.add_to_cart_button)
        return self

    @allure.step("Найти все ошибки валидации на странице")
    def collect_validation_errors(self):
        try:
            self.get_elements(self.validation_error)
            return True
        except TimeoutException:
            return False

    @allure.step("Кликнуть радио")
    def click_radio(self):
        self.click(self.radio_7)
        radio = self.get_element(self.radio_7)
        return radio.get_property("checked")

    @allure.step("Кликнуть чекбокс")
    def click_checkbox(self):
        self.click(self.checkbox_11)
        checkbox = self.get_element(self.checkbox_11)
        return checkbox.get_property("checked")

    @allure.step("Ввести значение в поле Text")
    def input_text(self, text):
        text_element = self.get_element(self.text_input)
        self.browser.execute_script("arguments[0].scrollIntoView()", text_element)
        time.sleep(0.5)
        self.input_value(self.text_input, text)
        text_val = self.get_element(self.text_input)
        return text_val.get_attribute("value")

    @allure.step("Выбрать значение в поле Select")
    def select_val(self, val):
        self.select(self.select_field, val)
        select = self.get_element(self.select_field)
        return select.get_property("value")

    @allure.step("Ввести значение в поле Textarea")
    def input_textarea(self, text):
        textarea_element = self.get_element(self.textarea)
        self.browser.execute_script("arguments[0].scrollIntoView()", textarea_element)
        self.input_value(self.textarea, text)
        textarea_val = self.get_element(self.textarea)
        return textarea_val.get_attribute("value")

    @allure.step("Загрузить файл")
    def upload_new_file(self, filepath):
        self.click(self.upload_file_button)
        if not self.browser.is_headless:
            try:
                import pyautogui
                time.sleep(1)
                pyautogui.press('esc')
            except Exception:
                print('Эта шляпа не работает при запуске теста из контейнера Docker')
        self.input_value(self.upload_file_input, filepath)
        return self.waiting_for_alert()

    @allure.step("Ввести дату")
    def date_input(self, date):
        self.input_value(self.date_input_element, date)
        date_val = self.get_element(self.date_input_element)
        return date_val.get_attribute("value")

    @allure.step("Ввести время")
    def time_input(self, time):
        self.input_value(self.time_input_element, time)
        time_val = self.get_element(self.time_input_element)
        return time_val.get_attribute("value")

    @allure.step("Ввести дату и время")
    def datetime_input(self, datetime):
        self.input_value(self.datetime_input_element, datetime)
        datetime_val = self.get_element(self.datetime_input_element)
        self.click(self.textarea)
        return datetime_val.get_attribute("value")

    @allure.step("Найти продукт в корзине")
    def find_product_in_cart(self):
        button = self.get_element(self.product_cart_button)
        self.browser.execute_script("arguments[0].scrollIntoView()", button)
        self.click(self.product_cart_button)
        try:
            self.get_element(self.product_in_cart)
            return True
        except TimeoutException:
            return False
