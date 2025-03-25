import contextlib
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import (InvalidElementStateException, NoAlertPresentException, InvalidArgumentException,
                                        ElementClickInterceptedException)

from diplom.pages.page_factory import PageFactory


class BasePage(PageFactory):
    def __init__(self, browser):
        super().__init__(browser)

    def _text_xpath(self, tag, text):
        return f"//{tag}[text()='{text}']"

    def get_element(self, element: object, timeout=5):
        self.logger.info("%s: Find element %s" % (self.class_name, element))
        if isinstance(element, tuple):
            return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(element))
        elif isinstance(element, WebElement):
            return WebDriverWait(self.browser, timeout).until(EC.visibility_of(element))
        else:
            raise ValueError("Ожидается tuple или WebElement")

    def get_elements(self, element: object, timeout=5):
        self.logger.info("%s: Find all elements %s" % (self.class_name, element))
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_all_elements_located(element))

    def click(self, element: object, timeout=5):
        self.logger.info("%s: Clicking element: %s" % (self.class_name, element))
        if isinstance(element, tuple):
            web_element = WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(element))
        elif isinstance(element, WebElement):
            web_element = element
        ActionChains(self.browser).move_to_element(web_element).pause(0.3).click().perform()

    def input_value(self, element: object, text: str, timeout=5):
        self.logger.info("%s: Input %s in input %s" % (self.class_name, text, element))
        if isinstance(element, tuple):
            web_element = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(element))
        elif isinstance(element, WebElement):
            web_element = element
        try:
            web_element.click()
        except (InvalidArgumentException, ElementClickInterceptedException):
            pass
        try:
            web_element.clear()
        except InvalidElementStateException:
            pass
        web_element.send_keys(text)

    def redirect(self, url):
        WebDriverWait(self.browser, 15).until(EC.url_changes(url))

    def select(self, element: object, value: str, timeout=5):
        self.logger.info("%s: Select %s from %s" % (self.class_name, value, element))
        if isinstance(element, tuple):
            select_element = WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(element))
        elif isinstance(element, WebElement):
            select_element = WebDriverWait(self.browser, timeout).until(EC.visibility_of(element))
        Select(select_element).select_by_value(value)

    def waiting_for_alert(self):
        self.logger.info("%s: Waiting for alert" % self.class_name)
        try:
            WebDriverWait(self.browser, 10).until(EC.alert_is_present())
            self.browser.switch_to.alert.accept()
            return True
        except NoAlertPresentException:
            return False

    @contextlib.contextmanager
    def switch_to_frame(self, element: object, timeout=5):
        self.logger.info("%s: Switching to iframe: %s" % (self.class_name, element))
        WebDriverWait(self.browser, timeout).until(EC.frame_to_be_available_and_switch_to_it(element))
        try:
            yield
        finally:
            self.browser.switch_to.default_content()
