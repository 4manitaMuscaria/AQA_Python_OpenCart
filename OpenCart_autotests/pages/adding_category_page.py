import time

import allure

from selenium.common.exceptions import TimeoutException
from OpenCart_autotests.pages.base_page import BasePage
from OpenCart_autotests.locators.adding_category_locators import AddingCategoryLocators


class AddingCategory(BasePage, AddingCategoryLocators):

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("Находим заголовок")
    def get_card_header(self):
        card_header = self.get_element(self.card_header)
        return card_header.text

    @allure.step("Закрываем бесячий алерт")
    def close_alert(self):
        try:
            self.click(self.close_alert_button)
        except TimeoutException:
            self.logger.info("Не нашли бесячий алерт")
        return self

    @allure.step("Вводим наименование")
    def input_category_name(self, name):
        self.input_value(self.category_name, name)
        category_val = self.get_element(self.category_name)
        return category_val.get_attribute("value")

    @allure.step("Вводим наименование тэга")
    def input_meta_title(self, title):
        meta = self.get_element(self.meta_title)
        self.browser.execute_script("arguments[0].scrollIntoView()", meta)
        time.sleep(0.5)
        self.input_value(self.meta_title, title)
        meta = self.get_element(self.meta_title)
        return meta.get_attribute("value")

    @allure.step("Вводим описание тэга")
    def input_meta_description(self, description):
        meta = self.get_element(self.meta_description)
        self.browser.execute_script("arguments[0].scrollIntoView()", meta)
        time.sleep(0.5)
        self.input_value(self.meta_description, description)
        meta = self.get_element(self.meta_description)
        return meta.get_attribute("value")

    @allure.step("Вводим ключевые слова тэга")
    def input_meta_keywords(self, keywords):
        meta = self.get_element(self.meta_keywords)
        self.browser.execute_script("arguments[0].scrollIntoView()", meta)
        time.sleep(0.5)
        self.input_value(self.meta_keywords, keywords)
        meta = self.get_element(self.meta_keywords)
        return meta.get_attribute("value")

    @allure.step("Переходим на вкладку Data")
    def go_to_data_tab(self):
        self.click(self.data_tab)
        datatab = self.get_element(self.data_tab)
        return datatab.get_attribute("aria-selected")

    @allure.step("Выбираем родительскую категорию")
    def select_parent(self):
        self.click(self.parent)
        self.click(self.parent_category)
        parent_value = self.get_element(self.parent)
        return parent_value.get_attribute("value")

    @allure.step("Кликаем кнопку Edit")
    def click_edit_button(self):
        self.click(self.edit_button)
        return self

    @allure.step("Находим загруженный элемент")
    def get_image(self):
        image = self.get_element(self.image)
        return image.get_attribute("src").split('/')[-1]

    @allure.step("Переходим на вкладку SEO")
    def go_to_seo_tab(self):
        self.click(self.seo_tab)
        seo_tab = self.get_element(self.seo_tab)
        return seo_tab.get_attribute("aria-selected")

    @allure.step("Вводим необходимые данные на вкладке SEO")
    def input_seo_url(self, keywords):
        self.input_value(self.seo_url, keywords)
        seo_url_val = self.get_element(self.seo_url)
        return seo_url_val.get_attribute("value")

    @allure.step("Сохраняем категорию")
    def save_category(self):
        self.click(self.save_button)
        success_alert = self.get_element(self.success_alert)
        return success_alert.text
