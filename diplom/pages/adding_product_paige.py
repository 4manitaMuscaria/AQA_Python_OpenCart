import time
import allure
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from hw_7.pages.base_page import BasePage


class AddingProduct(BasePage):
    CLOSE_ALERT_BUTTON = (By.CSS_SELECTOR, "div[role='alert']>a[title='Close']")
    PRODUCT_NAME_INPUT = (By.ID, "input-name-1")
    META_TAG_TITLE_INPUT = (By.ID, "input-meta-title-1")
    DATA_TAB = (By.XPATH, "//form[@id='form-product']//a[text()='Data']")
    MODEL_INPUT = (By.ID, "input-model")
    SEO_TAB = (By.XPATH, "//form[@id='form-product']//a[text()='SEO']")
    SEO_URL_INPUT = (By.ID, "input-keyword-0-1")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[title='Save']")

    @allure.step("Перейти на вкладку Data")
    def go_to_data_tab(self):
        self.click(self.DATA_TAB)
        return self

    @allure.step("Перейти на вкладку SEO")
    def go_to_seo_tab(self):
        self.click(self.SEO_TAB)
        return self

    @allure.step("Закрыть бесячий алерт")
    def close_alert(self):
        self.click(self.CLOSE_ALERT_BUTTON)
        return self

    @allure.step("Ввести необходимые данные на вкладке General")
    def input_general(self, product_name, meta_tag):
        self.input_value(self.PRODUCT_NAME_INPUT, product_name)
        meta = self.get_element(self.META_TAG_TITLE_INPUT)
        self.browser.execute_script("arguments[0].scrollIntoView()", meta)
        time.sleep(0.5)
        self.input_value(self.META_TAG_TITLE_INPUT, meta_tag)
        return self

    @allure.step("Ввести необходимые данные на вкладке Data")
    def input_data(self, model):
        self.input_value(self.MODEL_INPUT, model)
        return self

    @allure.step("Ввести необходимые данные на вкладке SEO")
    def input_seo_url(self, seo_url):
        self.input_value(self.SEO_URL_INPUT, seo_url)
        return self

    @allure.step("Нажать кнопку Сохранить")
    def save_product(self):
        try:
            self.click(self.SAVE_BUTTON)
            return True
        except NoSuchElementException:
            return False
