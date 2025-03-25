import time
import allure
import pyautogui


from diplom.pages.base_page import BasePage
from diplom.locators.file_manager_locators import FileManagerLocators


class FileManager(BasePage, FileManagerLocators):

    def __init__(self, browser):
        super().__init__(browser)
        self.iframe_element = self.get_element(self.file_manager)

    @allure.step("Получаем заголовок модального окна файл менеджера")
    def get_filemanager_title(self):
        title = self.get_element(self.file_manager_title)
        return title.text

    @allure.step("Загружаем свое изображение")
    def upload_file(self, filepath):
        self.click(self.upload_button)
        if not self.browser.is_headless:
            time.sleep(1)
            pyautogui.press('esc')
        self.input_value(self.upload_input, filepath)
        return self.waiting_for_alert()

    @allure.step("Выбираем загруженное изображение")
    def image_select(self):
        self.get_element(self.image)
        self.click(self.image)
        return self
