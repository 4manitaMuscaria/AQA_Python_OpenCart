from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from diplom.locators.alert_locators import AlertLocators


class AlertSuccessElement(AlertLocators):

    def __init__(self, browser):
        self.browser = browser
        self.alert = WebDriverWait(self.browser, 3).until(
            EC.visibility_of_element_located(self.alert_element))

    def alert_text(self):
        text_element = (WebDriverWait(self.alert, timeout=5).until
                        (EC.visibility_of_element_located(self.alert_text_element)))
        return text_element.text

    def remove_alert(self):
        element = WebDriverWait(self.alert, timeout=10).until(EC.presence_of_element_located(self.alert_remove))
        self.browser.execute_script("arguments[0].remove();", element)
        return self

