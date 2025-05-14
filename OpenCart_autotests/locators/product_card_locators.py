from selenium.webdriver.common.by import By


class ProductCardLocators:

    @property
    def product_name(self):
        return By.XPATH, "//div[@id='product-info']//h1"

    @property
    def add_to_cart_button(self):
        return By.XPATH, "//button[@id='button-cart']"

    @property
    def validation_error(self):
        return By.XPATH, "//div[contains(@id, 'error') and contains(text(), 'required!')]"

    @property
    def radio_7(self):
        return By.XPATH, "//input[@id='input-option-value-7']"

    @property
    def checkbox_11(self):
        return By.XPATH, "//input[@id='input-option-value-11']"

    @property
    def text_input(self):
        return By.XPATH, "//input[@id='input-option-208']"

    @property
    def select_field(self):
        return By.XPATH, "//select[@id='input-option-217']"

    @property
    def textarea(self):
        return By.XPATH, "//textarea[@id='input-option-209']"

    @property
    def upload_file_button(self):
        return By.XPATH, "//button[@id='button-upload-222']"

    @property
    def upload_file_input(self):
        return By.XPATH, "//input[@type='file']"

    @property
    def alert(self):
        return By.XPATH, "//div[@class='alert alert-success alert-dismissible']"

    @property
    def date_input_element(self):
        return By.XPATH, "//input[@id='input-option-219']"

    @property
    def time_input_element(self):
        return By.XPATH, "//input[@id='input-option-221']"

    @property
    def datetime_input_element(self):
        return By.XPATH, "//input[@id='input-option-220']"

    @property
    def product_cart_button(self):
        return By.XPATH, "//div[@id='header-cart']//button[@data-bs-toggle='dropdown']"

    @property
    def product_in_cart(self):
        return By.XPATH, "//div[@id='header-cart']//a[text()='Apple Cinema 30\"']"
