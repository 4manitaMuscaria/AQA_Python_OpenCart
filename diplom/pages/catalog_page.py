import allure

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from hw_7.pages.base_page import BasePage


class Catalog(BasePage):
    CONTENT = (By.CSS_SELECTOR, "#content")
    CART_BUTTON = (By.XPATH, "//button[.//text()[contains(., 'item')]]")
    CART_DROPDOWN = (By.CSS_SELECTOR, "#header-cart > div > ul")
    PRODUCT_THUMBS = (By.CSS_SELECTOR, ".product-thumb  h4 a")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".product-thumb  button[title='Add to Cart']")
    ADD_TO_WISHLIST_BUTTON = (By.CSS_SELECTOR, ".product-thumb  button[title='Add to Wish List']")
    ADD_TO_COMPARE_BUTTON = (By.CSS_SELECTOR, ".product-thumb  button[title='Compare this Product']")

    def __init__(self, browser):
        super().__init__(browser)
        browser.get(f"{browser.url}/en-gb/catalog/desktops")

    @allure.step("Ожидание перехода в раздел Desktops")
    def waiting_for_category(self):
        try:
            self.get_element((By.XPATH, self._text_xpath("h2", "Desktops")))
            return True
        except NoSuchElementException:
            return False

    @allure.step("Кликнуть по корзине")
    def click_cart_button(self):
        self.click(self.CART_BUTTON)
        try:
            self.get_element(self.CART_DROPDOWN)
            return True
        except NoSuchElementException:
            return False

    @allure.step("Получить наименование продукта")
    def get_product_name(self, index=0):
        return self.get_elements(self.PRODUCT_THUMBS)[index].text

    @allure.step("Кликнуть по кнопке Добавить в корзину")
    def click_add_to_cart(self, index=0):
        if index == 0:
            self.click(self.ADD_TO_CART_BUTTON)
        else:
            self.get_elements(self.ADD_TO_CART_BUTTON)[index].click()

    @allure.step("Кликнуть по кнопке Добавить в вишлист")
    def click_add_to_wishlist(self, index=0):
        if index == 0:
            self.click(self.ADD_TO_WISHLIST_BUTTON)
        else:
            self.get_elements(self.ADD_TO_WISHLIST_BUTTON)[index].click()

    @allure.step("Кликнуть по кнопке Добавить к сравнению")
    def click_add_to_compare(self, index=0):
        if index == 0:
            self.click(self.ADD_TO_COMPARE_BUTTON)
        else:
            self.get_elements(self.ADD_TO_COMPARE_BUTTON)[index].click()

    @allure.step("Проверить переход на страницу логина")
    def check_login_redirect(self):
        try:
            self.get_element((By.XPATH, "//div[@id='account-login']"))
            return True
        except NoSuchElementException:
            return False

    @allure.step("Проверить переход на страницу сравнения")
    def check_comparison_redirect(self):
        try:
            self.get_element((By.XPATH, "//div[@id='product-compare']"))
            return True
        except NoSuchElementException:
            return False
