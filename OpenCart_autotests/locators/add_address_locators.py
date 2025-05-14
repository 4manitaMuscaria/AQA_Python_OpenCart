from selenium.webdriver.common.by import By


class AddAddressLocators:

    @property
    def address_title(self):
        return By.XPATH, "//h1[text()='Add Address']"

    @property
    def first_name(self):
        return By.XPATH, "//input[@id='input-firstname']"

    @property
    def last_name(self):
        return By.XPATH, "//input[@id='input-lastname']"

    @property
    def address_1_input(self):
        return By.XPATH, "//input[@id='input-address-1']"

    @property
    def city_input(self):
        return By.XPATH, "//input[@id='input-city']"

    @property
    def country_select(self):
        return By.XPATH, "//select[@id='input-country']"

    @property
    def zone_select(self):
        return By.XPATH, "//select[@id='input-zone']"

    @property
    def continue_button(self):
        return By.XPATH, "//button[text()='Continue']"

    @property
    def validation_error(self):
        return By.XPATH, "//div[contains(@id, 'error') and contains(@class, 'block')]"
