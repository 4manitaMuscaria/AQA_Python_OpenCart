from selenium.webdriver.common.by import By


class FileManagerLocators:

    @property
    def file_manager(self):
        return By.XPATH, "//div[@id='filemanager']"

    @property
    def file_manager_title(self):
        return By.XPATH, "//div[@id='filemanager']//h5"

    @property
    def upload_button(self):
        return By.XPATH, "//button[@id='button-upload']"

    @property
    def upload_input(self):
        return By.XPATH, "//input[@type='file']"

    @property
    def image(self):
        return By.XPATH, "//img[@title='1.jpg']"
