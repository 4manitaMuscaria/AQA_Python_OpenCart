import allure

from OpenCart_autotests.pages.main_page import MainPage
from OpenCart_autotests.pages.account_register_paige import AccountRegister
from OpenCart_autotests.pages.my_account_page import MyAccount
from OpenCart_autotests.pages.add_address_page import AddAddress


@allure.epic('UI тесты')
@allure.story('Регистрация пользователя')
@allure.title('Проверка меню My Account')
def test_my_account_menu(browser):
    assert MainPage(browser).click_my_account()


@allure.epic('UI тесты')
@allure.story('Регистрация пользователя')
@allure.title('Проверка перехода на форму регистрации')
def test_register_account_opening(browser):
    MainPage(browser).click_my_account()
    MainPage(browser).open_register_account()
    assert AccountRegister(browser).get_title()


@allure.epic('UI тесты')
@allure.story('Регистрация пользователя')
@allure.title('Проверка ввода имени')
def test_firstname_input(browser, test_data):
    MainPage(browser).click_my_account()
    MainPage(browser).open_register_account()
    firstname = AccountRegister(browser).input_first_name(test_data.user_data["firstname"])
    assert firstname == test_data.user_data["firstname"]


@allure.epic('UI тесты')
@allure.story('Регистрация пользователя')
@allure.title('Проверка ввода фамилии')
def test_lastname_input(browser, test_data):
    MainPage(browser).click_my_account()
    MainPage(browser).open_register_account()
    lastname = AccountRegister(browser).input_last_name(test_data.user_data["lastname"])
    assert lastname == test_data.user_data["lastname"]


@allure.epic('UI тесты')
@allure.story('Регистрация пользователя')
@allure.title('Проверка ввода e-mail')
def test_email_input(browser, test_data):
    MainPage(browser).click_my_account()
    MainPage(browser).open_register_account()
    email = AccountRegister(browser).input_email(test_data.user_data["email"])
    assert email == test_data.user_data["email"]


@allure.epic('UI тесты')
@allure.story('Регистрация пользователя')
@allure.title('Проверка ввода пароля')
def test_password_input(browser, test_data):
    MainPage(browser).click_my_account()
    MainPage(browser).open_register_account()
    password = AccountRegister(browser).input_password(test_data.user_data["password"])
    assert password == test_data.user_data["password"]


@allure.epic('UI тесты')
@allure.story('Регистрация пользователя')
@allure.title('Проверка чекбокса Privacy Policy')
def test_privacy_policy_checkbox(browser):
    MainPage(browser).click_my_account()
    MainPage(browser).open_register_account()
    assert AccountRegister(browser).click_privacy_policy_submit()


@allure.epic('UI тесты')
@allure.story('Регистрация пользователя')
@allure.title('Проверка регистрации пользователя')
def test_user_registration(browser, test_data, delete_user):
    MainPage(browser).click_my_account()
    MainPage(browser).open_register_account()
    AccountRegister(browser).input_first_name(test_data.user_data["firstname"])
    AccountRegister(browser).input_last_name(test_data.user_data["lastname"])
    AccountRegister(browser).input_email(test_data.user_data["email"])
    AccountRegister(browser).input_password(test_data.user_data["password"])
    AccountRegister(browser).click_privacy_policy_submit()
    AccountRegister(browser).click_continue_button()
    assert AccountRegister(browser).get_success_message()


@allure.epic('UI тесты')
@allure.story('Регистрация пользователя')
@allure.title('Проверка перехода в мой аккаунт')
def test_my_account_opening(browser, delete_user, user_registration):
    assert MyAccount(browser).get_my_account_title()


@allure.epic('UI тесты')
@allure.story('Регистрация пользователя')
@allure.title('Проверка перехода в адресную книгу')
def test_address_book_modify(browser, delete_user, user_registration):
    MyAccount(browser).open_address_book()
    assert MyAccount(browser).get_address_book_title()


@allure.epic('UI тесты')
@allure.story('Регистрация пользователя')
@allure.title('Проверка перехода в адресную книгу')
def test_add_address_opening(browser, delete_user, user_registration):
    MyAccount(browser).open_address_book()
    MyAccount(browser).click_new_address()
    assert AddAddress(browser).get_add_address_title()


@allure.epic('UI тесты')
@allure.story('Регистрация пользователя')
@allure.title('Проверка ввода адреса')
def test_address_input(browser, test_data, delete_user, user_registration):
    MyAccount(browser).open_address_book()
    MyAccount(browser).click_new_address()
    address = AddAddress(browser).address_input(test_data.address_data["address"])
    assert address == test_data.address_data["address"]


@allure.epic('UI тесты')
@allure.story('Регистрация пользователя')
@allure.title('Проверка выбора страны')
def test_country_select(browser, test_data, delete_user, user_registration):
    MyAccount(browser).open_address_book()
    MyAccount(browser).click_new_address()
    country = AddAddress(browser).select_country(test_data.address_data["country"])
    assert country == test_data.address_data["country"]


@allure.epic('UI тесты')
@allure.story('Регистрация пользователя')
@allure.title('Проверка заполнения формы')
def test_set_address(browser, test_data, delete_user, delete_address, user_registration):
    MyAccount(browser).open_address_book()
    MyAccount(browser).click_new_address()
    validation_errors = AddAddress(browser).set_address_form_values(test_data.address_data["firstname"],
                                                                    test_data.address_data["lastname"],
                                                                    test_data.address_data["address"],
                                                                    test_data.address_data["city"],
                                                                    test_data.address_data["country"],
                                                                    test_data.address_data["zone"])
    assert not validation_errors


@allure.epic('UI тесты')
@allure.story('Регистрация пользователя')
@allure.title('Проверка добавления адреса')
def test_check_address_adding(browser, test_data, delete_user, delete_address, user_registration):
    MyAccount(browser).open_address_book()
    MyAccount(browser).click_new_address()
    AddAddress(browser).set_address_form_values(test_data.address_data["firstname"],
                                                test_data.address_data["lastname"],
                                                test_data.address_data["address"],
                                                test_data.address_data["city"],
                                                test_data.address_data["country"],
                                                test_data.address_data["zone"])
    assert test_data.address_data["address"] in MyAccount(browser).get_address()
