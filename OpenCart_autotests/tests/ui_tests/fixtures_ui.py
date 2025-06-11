import pytest

from sqlalchemy import text
from OpenCart_autotests.pages.login_admin_page import LoginAdmin
from OpenCart_autotests.config.credentials import Credentials
from OpenCart_autotests.pages.admin_account_page import AdminAccount
from OpenCart_autotests.pages.main_page import MainPage
from OpenCart_autotests.pages.account_register_paige import AccountRegister
from OpenCart_autotests.src.test_data import _TestData


@pytest.fixture()
def authenticate(browser):
    LoginAdmin(browser) \
        .login_input(Credentials.ADMIN_LOGIN["username"]) \
        .password_input(Credentials.ADMIN_LOGIN["password"]) \
        .click_login_button()
    AdminAccount(browser).wait_logged_in()


@pytest.fixture(scope="session")
def test_data():
    return _TestData()


@pytest.fixture()
def user_registration(browser, test_data):
    MainPage(browser).click_my_account()
    MainPage(browser).open_register_account()
    AccountRegister(browser).input_first_name(test_data.user_data["firstname"])
    AccountRegister(browser).input_last_name(test_data.user_data["lastname"])
    AccountRegister(browser).input_email(test_data.user_data["email"])
    AccountRegister(browser).input_password(test_data.user_data["password"])
    AccountRegister(browser).click_privacy_policy_submit()
    AccountRegister(browser).click_continue_button()
    AccountRegister(browser).get_success_message()
    AccountRegister(browser).click_continue_element()

    # yield


@pytest.fixture()
def delete_user(logger, models, db_session, test_data):

    yield

    logger.info(f"Deleting user {test_data.user_data["email"]} from database...")
    # db_models_and_session.execute(text("DELETE FROM oc_customer WHERE email = :email"),
    #                               {"email": test_data.user_data["email"]})
    # db_models_and_session.commit()
    customer = models["oc_customer"]
    db_session.query(customer).filter(customer.email == test_data.user_data["email"]).delete()
    db_session.commit()


@pytest.fixture()
def delete_address(logger, models, db_session, test_data):

    yield

    logger.info(f"Deleting address {test_data.address_data["address"]} from database...")
    # db_models_and_session.execute(text("DELETE FROM oc_address WHERE address_1 = :address"),
    #                               {"address": test_data.address_data["address"]})
    # db_models_and_session.commit()
    address = models["oc_address"]
    db_session.query(address).filter(address.address_1 == test_data.address_data["address"]).delete()
    db_session.commit()


@pytest.fixture()
def delete_category(logger, models, db_session, test_data):

    yield

    logger.info(f"Deleting category {test_data.category_data["category_name"]} from database...")
    # db_models_and_session.execute(text(
    #     "DELETE c, cd FROM oc_category c JOIN oc_category_description cd ON c.category_id = cd.category_id WHERE "
    #     "cd.name = :name"), {"name": test_data.category_data["category_name"]})
    # db_models_and_session.execute(text("DELETE s FROM oc_seo_url s WHERE s.keyword LIKE :keyword"),
    #                               {"keyword": f"%{test_data.category_data["seo_url"]}"})
    # db_models_and_session.commit()
    CategoryDescription = models["oc_category_description"]
    Category = models["oc_category"]
    SeoUrl = models["oc_seo_url"]

    category = (db_session.query(Category)
                .join(CategoryDescription, Category.category_id == CategoryDescription.category_id)
                .filter(CategoryDescription.name == test_data.category_data["category_name"]).first())

    if category:
        db_session.delete(category)

    db_session.query(SeoUrl).filter(
        SeoUrl.keyword.like(f"%{test_data.category_data['seo_url']}")
    ).delete(synchronize_session=False)


@pytest.fixture()
def delete_file(logger, models, db_session, test_data):

    yield

    logger.info(f"Deleting uploaded file from database...")
    # db_models_and_session.execute(text("DELETE FROM oc_upload WHERE name = :name"),
    #                               {"name": "1.jpg"})
    upload = models["oc_upload"]
    db_session.query(upload).filter(upload.name == "1.jpg").delete()
    db_session.commit()
