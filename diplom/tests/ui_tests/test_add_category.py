import allure

from diplom.pages.admin_account_page import AdminAccount
from diplom.pages.adding_category_page import AddingCategory
from diplom.pages.categories_page import Categories
from diplom.pages.iframe_element import IframeElement
from diplom.pages.file_manager_element import FileManager


@allure.epic('UI тесты')
@allure.story('Добавление категории товаров')
@allure.title('Проверка меню Каталог')
def test_catalog_menu(browser, authenticate):
    assert AdminAccount(browser).click_catalog()


@allure.epic('UI тесты')
@allure.story('Добавление категории товаров')
@allure.title('Проверка перехода в раздел Категории')
def test_categories_opening(browser, authenticate):
    AdminAccount(browser).click_catalog()
    AdminAccount(browser).click_categories()
    AdminAccount(browser).waiting_for_page("Categories")


@allure.epic('UI тесты')
@allure.story('Добавление категории товаров')
@allure.title('Проверка перехода в карточку Категории')
def test_category_card_opening(browser, authenticate):
    AdminAccount(browser).click_catalog()
    AdminAccount(browser).click_categories()
    Categories(browser).add_new()
    assert "Add Category" in AddingCategory(browser).get_card_header()


@allure.epic('UI тесты')
@allure.story('Добавление категории товаров')
@allure.title('Проверка ввода наименования Категории')
def test_input_category_name(browser, authenticate, test_data):
    AdminAccount(browser).click_catalog()
    AdminAccount(browser).click_categories()
    Categories(browser).add_new()
    AddingCategory(browser).close_alert()
    category_name = AddingCategory(browser).input_category_name(test_data.category_data["category_name"])
    assert category_name == test_data.category_data["category_name"]


@allure.epic('UI тесты')
@allure.story('Добавление категории товаров')
@allure.title('Проверка ввода описания Категории')
def test_input_category_description(browser, authenticate, test_data):
    AdminAccount(browser).click_catalog()
    AdminAccount(browser).click_categories()
    Categories(browser).add_new()
    AddingCategory(browser).close_alert()
    description = IframeElement(browser).input_description(test_data.category_data["description"])
    assert description == test_data.category_data["description"]


@allure.epic('UI тесты')
@allure.story('Добавление категории товаров')
@allure.title('Проверка ввода наименования тэга')
def test_input_meta_title(browser, authenticate, test_data):
    AdminAccount(browser).click_catalog()
    AdminAccount(browser).click_categories()
    Categories(browser).add_new()
    AddingCategory(browser).close_alert()
    meta_title = AddingCategory(browser).input_meta_title(test_data.category_data["meta_title"])
    assert meta_title == test_data.category_data["meta_title"]


@allure.epic('UI тесты')
@allure.story('Добавление категории товаров')
@allure.title('Проверка ввода описания тэга')
def test_input_meta_description(browser, authenticate, test_data):
    AdminAccount(browser).click_catalog()
    AdminAccount(browser).click_categories()
    Categories(browser).add_new()
    AddingCategory(browser).close_alert()
    meta_description = AddingCategory(browser).input_meta_description(test_data.category_data["meta_description"])
    assert meta_description == test_data.category_data["meta_description"]


@allure.epic('UI тесты')
@allure.story('Добавление категории товаров')
@allure.title('Проверка ввода описания тэга')
def test_input_meta_keywords(browser, authenticate, test_data):
    AdminAccount(browser).click_catalog()
    AdminAccount(browser).click_categories()
    Categories(browser).add_new()
    AddingCategory(browser).close_alert()
    meta_keywords = AddingCategory(browser).input_meta_keywords(test_data.category_data["meta_keywords"])
    assert meta_keywords == test_data.category_data["meta_keywords"]


@allure.epic('UI тесты')
@allure.story('Добавление категории товаров')
@allure.title('Проверка перехода на вкладку Data')
def test_data_tab_opening(browser, authenticate):
    AdminAccount(browser).click_catalog()
    AdminAccount(browser).click_categories()
    Categories(browser).add_new()
    assert AddingCategory(browser).go_to_data_tab()


@allure.epic('UI тесты')
@allure.story('Добавление категории товаров')
@allure.title('Проверка выбора родительской категории')
def test_select_parent(browser, authenticate):
    AdminAccount(browser).click_catalog()
    AdminAccount(browser).click_categories()
    Categories(browser).add_new()
    AddingCategory(browser).go_to_data_tab()
    parent = AddingCategory(browser).select_parent()
    assert "Components" in parent


@allure.epic('UI тесты')
@allure.story('Добавление категории товаров')
@allure.title('Проверка модального окна с выбором изображения')
def test_filemanager_opening(browser, authenticate):
    AdminAccount(browser).click_catalog()
    AdminAccount(browser).click_categories()
    Categories(browser).add_new()
    AddingCategory(browser).go_to_data_tab()
    AddingCategory(browser).click_edit_button()
    assert "Image Manager" in FileManager(browser).get_filemanager_title()


@allure.epic('UI тесты')
@allure.story('Добавление категории товаров')
@allure.title('Проверка загрузки изображения')
def test_upload_image(browser, authenticate, test_data, db_session):
    AdminAccount(browser).click_catalog()
    AdminAccount(browser).click_categories()
    Categories(browser).add_new()
    AddingCategory(browser).go_to_data_tab()
    AddingCategory(browser).click_edit_button()
    assert FileManager(browser).upload_file(test_data.get_filepath)


@allure.epic('UI тесты')
@allure.story('Добавление категории товаров')
@allure.title('Проверка выбора загруженного изображения')
def test_image_select(browser, authenticate, test_data, db_session):
    AdminAccount(browser).click_catalog()
    AdminAccount(browser).click_categories()
    Categories(browser).add_new()
    AddingCategory(browser).go_to_data_tab()
    AddingCategory(browser).click_edit_button()
    FileManager(browser).upload_file(test_data.get_filepath)
    FileManager(browser).image_select()
    assert AddingCategory(browser).get_image() == "1-136x136.jpg"


@allure.epic('UI тесты')
@allure.story('Добавление категории товаров')
@allure.title('Проверка перехода на вкладку SEO')
def test_seo_tab_opening(browser, authenticate):
    AdminAccount(browser).click_catalog()
    AdminAccount(browser).click_categories()
    Categories(browser).add_new()
    assert AddingCategory(browser).go_to_seo_tab()


@allure.epic('UI тесты')
@allure.story('Добавление категории товаров')
@allure.title('Проверка ввода данных SEO')
def test_seo_url_input(browser, authenticate, test_data):
    AdminAccount(browser).click_catalog()
    AdminAccount(browser).click_categories()
    Categories(browser).add_new()
    AddingCategory(browser).go_to_seo_tab()
    seo_url = AddingCategory(browser).input_seo_url(test_data.category_data["seo_url"])
    assert seo_url == test_data.category_data["seo_url"]


@allure.epic('UI тесты')
@allure.story('Добавление категории товаров')
@allure.title('Проверка создания новой категории')
def test_category_creation(browser, authenticate, test_data, db_session):
    AdminAccount(browser).click_catalog()
    AdminAccount(browser).click_categories()
    Categories(browser).add_new()
    AddingCategory(browser).close_alert()
    AddingCategory(browser).input_category_name(test_data.category_data["category_name"])
    IframeElement(browser).input_description(test_data.category_data["description"])
    AddingCategory(browser).input_meta_title(test_data.category_data["meta_title"])
    AddingCategory(browser).input_meta_description(test_data.category_data["meta_description"])
    AddingCategory(browser).input_meta_keywords(test_data.category_data["meta_keywords"])
    AddingCategory(browser).go_to_data_tab()
    AddingCategory(browser).select_parent()
    AddingCategory(browser).click_edit_button()
    FileManager(browser).upload_file(test_data.get_filepath)
    FileManager(browser).image_select()
    AddingCategory(browser).go_to_seo_tab()
    AddingCategory(browser).input_seo_url(test_data.category_data["seo_url"])
    assert "Success: You have modified categories!" in AddingCategory(browser).save_category()
