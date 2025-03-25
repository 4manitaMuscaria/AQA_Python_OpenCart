from selenium.webdriver.common.by import By


class CategoriesLocators:

    @property
    def add_new_button(self):
        return By.XPATH, "//a[@title='Add New']"
