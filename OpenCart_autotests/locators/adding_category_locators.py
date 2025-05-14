from selenium.webdriver.common.by import By


class AddingCategoryLocators:

    @property
    def card_header(self):
        return By.XPATH, "//div[@class='card-header']"

    @property
    def category_name(self):
        return By.XPATH, "//input[@id='input-name-1']"

    @property
    def meta_title(self):
        return By.XPATH, "//input[@id='input-meta-title-1']"

    @property
    def meta_description(self):
        return By.XPATH, "//textarea[@id='input-meta-description-1']"

    @property
    def meta_keywords(self):
        return By.XPATH, "//textarea[@id='input-meta-keyword-1']"

    @property
    def data_tab(self):
        return By.XPATH, "//form[@id='form-category']//a[text()='Data']"

    @property
    def parent(self):
        return By.XPATH, "//input[@id='input-parent']"

    @property
    def edit_button(self):
        return By.XPATH, "//button[text()=' Edit']"

    @property
    def image(self):
        return By.XPATH, "//img[@id='thumb-image']"

    @property
    def seo_tab(self):
        return By.XPATH, "//form[@id='form-category']//a[text()='SEO']"

    @property
    def seo_url(self):
        return By.XPATH, "//input[@id='input-keyword-0-1']"

    @property
    def save_button(self):
        return By.XPATH, "//button[@type='submit']"

    @property
    def close_alert_button(self):
        return By.XPATH, "//div[@role='alert']/a[@title='Close']"

    @property
    def parent_category(self):
        return By.XPATH, "//ul[@id='autocomplete-parent']//a[text()='Components']"

    @property
    def success_alert(self):
        return By.XPATH, "//div[@id='alert']/div"
