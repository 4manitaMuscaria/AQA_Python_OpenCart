import pytest
import json
import requests
import allure

from pydantic import ValidationError
from sqlalchemy import text
from OpenCart_autotests.models.cart_response_model import CartResponse


@allure.epic('API тесты')
@allure.story('Просмотр корзины')
@allure.title('Проверка статуса')
def test_checkout_cart_status(logger, base_url, get_api_token, add_voucher, delete_session):
    target_url = f"{base_url}?route=api/sale/cart&api_token={get_api_token}"

    payload = {}
    headers = {}

    logger.info("Sending request")
    response = requests.request("GET", target_url, headers=headers, data=payload, verify=False)
    assert response.status_code == 200


@allure.epic('API тесты')
@allure.story('Просмотр корзины')
@allure.title('Валидация ответа')
def test_checkout_cart_validate(logger, base_url, get_api_token, add_voucher, delete_session):
    target_url = f"{base_url}?route=api/sale/cart&api_token={get_api_token}"

    payload = {}
    headers = {}

    logger.info("Sending request")
    response = requests.request("GET", target_url, headers=headers, data=payload, verify=False).json()

    logger.info("Validating response")
    try:
        validated_data = CartResponse(**response)
        assert len(validated_data.vouchers) == 1
    except ValidationError as e:
        pytest.fail(f"Validation failed: {e}")


@allure.epic('API тесты')
@allure.story('Просмотр корзины')
@allure.title('Проверка данных')
def test_checkout_cart_data(logger, models, db_session, base_url, get_api_token, add_voucher, delete_session):
    target_url = f"{base_url}?route=api/sale/cart&api_token={get_api_token}"

    payload = {}
    headers = {}

    logger.info("Sending request")
    response = requests.request("GET", target_url, headers=headers, data=payload, verify=False).json()

    logger.info("Validating response")
    try:
        validated_data = CartResponse(**response)
        assert len(validated_data.vouchers) == 1
    except ValidationError as e:
        pytest.fail(f"Validation failed: {e}")

    logger.info(f"Getting session {get_api_token} data from DB")
    # session_data_raw = db_models_and_session.execute(text("SELECT data FROM oc_session WHERE session_id = :session_id"),
    #                                                  {"session_id": get_api_token}).scalar()
    session = models["oc_session"]
    session_data_raw = db_session.query(session.data).filter(session.session_id == get_api_token).scalar()
    session_data = json.loads(session_data_raw)

    assert ((validated_data.vouchers[0].description == session_data['vouchers'][0]['description']) and
            (validated_data.vouchers[0].amount == session_data['vouchers'][0]['amount']))