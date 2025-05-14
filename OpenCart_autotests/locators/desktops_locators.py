from selenium.webdriver.common.by import By


class DesktopsLocators:

    @property
    def title(self):
        return By.XPATH, "//div[@id='content']/h2"

    @property
    def product_link(self):
        return By.XPATH, "//a[text()='Apple Cinema 30\"']"
