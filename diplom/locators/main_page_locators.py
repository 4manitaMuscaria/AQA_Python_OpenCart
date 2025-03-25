from selenium.webdriver.common.by import By


class MainPageLocators:
    @property
    def desktops_link(self):
        return By.XPATH, "//div[@id='narbar-menu']//a[text()='Desktops']"

    @property
    def desktops_dropdown(self):
        return By.XPATH, "//div[@id='narbar-menu']//a[text()='Desktops']/../div"

    @property
    def all_desktops_link(self):
        return By.XPATH, "//div[@id='narbar-menu']//a[text()='Show All Desktops']"

    @property
    def my_account(self):
        return By.XPATH, "//span[text()='My Account']/.."

    @property
    def register(self):
        return By.XPATH, "//a[text()='Register']"
