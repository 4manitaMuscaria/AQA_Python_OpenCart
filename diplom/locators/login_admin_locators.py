from selenium.webdriver.common.by import By


class LoginAdminLocators:

    @property
    def username(self):
        return By.XPATH, "//input[@id='input-username']"

    @property
    def password(self):
        return By.XPATH, "//input[@id='input-password']"

    @property
    def login_button(self):
        return By.XPATH, "//button[text()=' Login']"
