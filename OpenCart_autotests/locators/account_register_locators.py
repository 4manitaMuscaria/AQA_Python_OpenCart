from selenium.webdriver.common.by import By


class AccountRegisterLocators:

    @property
    def title(self):
        return By.XPATH, "//h1[text()='Register Account']"

    @property
    def first_name(self):
        return By.XPATH, "//input[@id='input-firstname']"

    @property
    def last_name(self):
        return By.XPATH, "//input[@id='input-lastname']"

    @property
    def email_element(self):
        return By.XPATH, "//input[@id='input-email']"

    @property
    def password_element(self):
        return By.XPATH, "//input[@id='input-password']"

    @property
    def privacy_policy(self):
        return By.XPATH, "//input[@name='agree']"

    @property
    def continue_button(self):
        return By.XPATH, "//button[text()='Continue']"

    @property
    def success_message(self):
        return By.XPATH, "//h1[text()='Your Account Has Been Created!']"

    @property
    def continue_element(self):
        return By.XPATH, "//a[text()='Continue']"
