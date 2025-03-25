from selenium.webdriver.common.by import By


class MyAccountLocators:

    @property
    def account_title(self):
        return By.XPATH, "//h2[text()='My Account']"

    @property
    def address_book_link(self):
        return By.XPATH, "//a[text()='Modify your address book entries']"

    @property
    def address_book_title(self):
        return By.XPATH, "//h1[text()='Address Book Entries']"

    @property
    def new_address_button(self):
        return By.XPATH, "//a[text()='New Address']"

    @property
    def address_element(self):
        return By.XPATH, "//div[@id='address']//table//td[@class='text-start']"
