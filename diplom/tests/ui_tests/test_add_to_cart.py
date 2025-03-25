import allure

from diplom.pages.main_page import MainPage
from diplom.pages.desktops_page import Desktops
from diplom.pages.product_card_page import ProductCard
from diplom.elements.alert_element import AlertSuccessElement


@allure.epic('UI тесты')
@allure.story('Добавление товара в корзину')
@allure.title('Проверка меню Desctops')
def test_desktops_menu(browser):
    assert MainPage(browser).click_desktops() == "static"


@allure.epic('UI тесты')
@allure.story('Добавление товара в корзину')
@allure.title('Проверка меню Desctops')
def test_desktops_opening(browser):
    MainPage(browser).click_desktops()
    MainPage(browser).click_all_desktops()
    assert Desktops(browser).get_title() == "Desktops"


@allure.epic('UI тесты')
@allure.story('Добавление товара в корзину')
@allure.title('Проверка перехода в карточку товара')
def test_product_card_opening(browser):
    MainPage(browser).click_desktops()
    MainPage(browser).click_all_desktops()
    Desktops(browser).go_to_product()
    assert "Apple Cinema 30\"" in ProductCard(browser).waiting_for_product_card()


@allure.epic('UI тесты')
@allure.story('Добавление товара в корзину')
@allure.title('Проверка валидации обязательных полей')
def test_form_validation(browser):
    MainPage(browser).click_desktops()
    MainPage(browser).click_all_desktops()
    Desktops(browser).go_to_product()
    ProductCard(browser).click_add_to_cart()
    assert ProductCard(browser).collect_validation_errors()


@allure.epic('UI тесты')
@allure.story('Добавление товара в корзину')
@allure.title('Проверка выбора радиобатона')
def test_radio(browser):
    MainPage(browser).click_desktops()
    MainPage(browser).click_all_desktops()
    Desktops(browser).go_to_product()
    assert ProductCard(browser).click_radio()


@allure.epic('UI тесты')
@allure.story('Добавление товара в корзину')
@allure.title('Проверка выбора чекбокса')
def test_radio(browser):
    MainPage(browser).click_desktops()
    MainPage(browser).click_all_desktops()
    Desktops(browser).go_to_product()
    assert ProductCard(browser).click_checkbox()


@allure.epic('UI тесты')
@allure.story('Добавление товара в корзину')
@allure.title('Проверка ввода текста Text')
def test_text_input(browser, test_data):
    MainPage(browser).click_desktops()
    MainPage(browser).click_all_desktops()
    Desktops(browser).go_to_product()
    text = ProductCard(browser).input_text(test_data.product_data["text"])
    assert text == test_data.product_data["text"]


@allure.epic('UI тесты')
@allure.story('Добавление товара в корзину')
@allure.title('Проверка выбора Select')
def test_select(browser, test_data):
    MainPage(browser).click_desktops()
    MainPage(browser).click_all_desktops()
    Desktops(browser).go_to_product()
    select = ProductCard(browser).select_val(test_data.product_data["select"])
    assert select == test_data.product_data["select"]


@allure.epic('UI тесты')
@allure.story('Добавление товара в корзину')
@allure.title('Проверка ввода текста Textarea')
def test_textarea_input(browser, test_data):
    MainPage(browser).click_desktops()
    MainPage(browser).click_all_desktops()
    Desktops(browser).go_to_product()
    text = ProductCard(browser).input_textarea(test_data.product_data["textarea"])
    assert text == test_data.product_data["textarea"]


@allure.epic('UI тесты')
@allure.story('Добавление товара в корзину')
@allure.title('Проверка загрузки файла')
def test_file_upload(browser, test_data, delete_file):
    MainPage(browser).click_desktops()
    MainPage(browser).click_all_desktops()
    Desktops(browser).go_to_product()
    file = ProductCard(browser).upload_new_file(test_data.get_filepath)
    assert file


@allure.epic('UI тесты')
@allure.story('Добавление товара в корзину')
@allure.title('Проверка ввода даты')
def test_date_input(browser, test_data):
    MainPage(browser).click_desktops()
    MainPage(browser).click_all_desktops()
    Desktops(browser).go_to_product()
    date = ProductCard(browser).date_input(test_data.product_data["date"])
    assert date == test_data.product_data["date"]


@allure.epic('UI тесты')
@allure.story('Добавление товара в корзину')
@allure.title('Проверка ввода времени')
def test_time_input(browser, test_data):
    MainPage(browser).click_desktops()
    MainPage(browser).click_all_desktops()
    Desktops(browser).go_to_product()
    time = ProductCard(browser).time_input(test_data.product_data["time"])
    assert time == test_data.product_data["time"]


@allure.epic('UI тесты')
@allure.story('Добавление товара в корзину')
@allure.title('Проверка ввода даты и времени')
def test_time_input(browser, test_data):
    MainPage(browser).click_desktops()
    MainPage(browser).click_all_desktops()
    Desktops(browser).go_to_product()
    date_time = ProductCard(browser).datetime_input(test_data.product_data["datetime"])
    assert date_time == test_data.product_data["datetime"]


@allure.epic('UI тесты')
@allure.story('Добавление товара в корзину')
@allure.title('Проверка добавления товара в корзину')
def test_adding_product_to_cart(browser, test_data, delete_file):
    MainPage(browser).click_desktops()
    MainPage(browser).click_all_desktops()
    Desktops(browser).go_to_product()
    ProductCard(browser).click_radio()
    ProductCard(browser).click_checkbox()
    ProductCard(browser).input_text(test_data.product_data["text"])
    ProductCard(browser).select_val(test_data.product_data["select"])
    ProductCard(browser).input_textarea(test_data.product_data["textarea"])
    ProductCard(browser).upload_new_file(test_data.get_filepath)
    ProductCard(browser).date_input(test_data.product_data["date"])
    ProductCard(browser).time_input(test_data.product_data["time"])
    ProductCard(browser).datetime_input(test_data.product_data["datetime"])
    ProductCard(browser).click_add_to_cart()
    alert_message = AlertSuccessElement(browser).alert_text()
    assert "Success: You have added" in alert_message


@allure.epic('UI тесты')
@allure.story('Добавление товара в корзину')
@allure.title('Проверка наличия продукта в корзине')
def test_product_in_cart(browser, test_data, delete_file):
    MainPage(browser).click_desktops()
    MainPage(browser).click_all_desktops()
    Desktops(browser).go_to_product()
    ProductCard(browser).click_radio()
    ProductCard(browser).click_checkbox()
    ProductCard(browser).input_text(test_data.product_data["text"])
    ProductCard(browser).select_val(test_data.product_data["select"])
    ProductCard(browser).input_textarea(test_data.product_data["textarea"])
    ProductCard(browser).upload_new_file(test_data.get_filepath)
    ProductCard(browser).date_input(test_data.product_data["date"])
    ProductCard(browser).time_input(test_data.product_data["time"])
    ProductCard(browser).datetime_input(test_data.product_data["datetime"])
    ProductCard(browser).click_add_to_cart()
    AlertSuccessElement(browser).remove_alert()
    assert ProductCard(browser).find_product_in_cart()


