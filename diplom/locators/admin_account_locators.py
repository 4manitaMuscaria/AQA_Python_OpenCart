from selenium.webdriver.common.by import By


class AdminAccountLocators:

    @property
    def logout_link(self):
        return By.XPATH, "//li[@id='nav-logout']"

    @property
    def catalog(self):
        return By.XPATH, "//li[@id = 'menu-catalog']/a"

    @property
    def categories(self):
        return By.XPATH, "//a[text()='Categories']"
