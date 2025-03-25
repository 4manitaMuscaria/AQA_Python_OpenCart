import allure

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from diplom.pages.base_page import BasePage
from diplom.locators.admin_account_locators import AdminAccountLocators


class AdminAccount(BasePage,AdminAccountLocators):

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("Ожидать авторизации")
    def wait_logged_in(self):
        self.get_element(self.logout_link)
        return self

    @allure.step("Кликнуть Каталог")
    def click_catalog(self):
        self.click(self.catalog)
        catalog_expanded = self.get_element(self.catalog)
        return catalog_expanded.get_attribute("aria-expanded")

    @allure.step("Кликнуть Категории")
    def click_categories(self):
        self.click(self.categories)
        return self

    @allure.step("Ожидать перехода на новую страницу")
    def waiting_for_page(self, page_name):
        try:
            self.get_element((By.XPATH, self._text_xpath("h1", page_name)))
            return True
        except TimeoutException:
            return False
