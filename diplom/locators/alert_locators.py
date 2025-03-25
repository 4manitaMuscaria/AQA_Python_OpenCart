from selenium.webdriver.common.by import By


class AlertLocators:

    @property
    def alert_element(self):
        return By.XPATH, "//div[@id='alert']"

    @property
    def alert_text_element(self):
        return By.XPATH, "//div[@id='alert']/div"

    @property
    def alert_remove(self):
        return By.XPATH, "//div[@id='alert']/div"
