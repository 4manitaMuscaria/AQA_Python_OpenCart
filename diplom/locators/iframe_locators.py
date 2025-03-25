from selenium.webdriver.common.by import By


class IframeLocators:

    @property
    def iframe(self):
        return By.XPATH, "//iframe"

    @property
    def description(self):
        return By.XPATH, "//p"
