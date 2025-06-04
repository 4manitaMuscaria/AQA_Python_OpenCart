import pytest
import json
import requests
import allure

from pydantic import ValidationError
from OpenCart_autotests.models import AddCustomerResponse, AddCustomerRequest


@allure.epic('API тесты')
@allure.story('Добавление покупателя')
@allure.title('Проверка статуса')
def test_add_customer_status(logger, base_url, get_api_token, test_data, delete_session):
    target_url = f"{base_url}?route=api/sale/customer&api_token={get_api_token}"

    try:
        payload = AddCustomerRequest(**test_data.user_data)
    except ValidationError as e:
        logger.error(f"Data validation failed: {e}")

    headers = {}

    logger.info("Sending request")
    response = requests.request("POST", target_url, headers=headers, data=payload.model_dump(), verify=False)
    assert response.status_code == 200


@allure.epic('API тесты')
@allure.story('Добавление покупателя')
@allure.title('Валидация ответа')
def test_add_customer_validate(logger, base_url, delete_session, get_api_token, test_data):
    target_url = f"{base_url}?route=api/sale/customer&api_token={get_api_token}"

    try:
        payload = AddCustomerRequest(**test_data.user_data)
    except ValidationError as e:
        logger.error(f"Data validation failed: {e}")

    headers = {}

    logger.info("Sending request")
    response = requests.request("POST", target_url, headers=headers, data=payload.model_dump(), verify=False).json()

    logger.info("Validating response")
    try:
        validated_data = AddCustomerResponse(**response)
        assert isinstance(validated_data, AddCustomerResponse), "Ответ не валиден по схеме AddVoucherResponse"
    except ValidationError as e:
        pytest.fail(f"Ошибка валидации {e.json()}")


@allure.epic('API тесты')
@allure.story('Добавление покупателя')
@allure.title('Проверка сохраненных данных')
def test_add_customer_data(logger, models, db_session, base_url, get_api_token, test_data, delete_session):
    target_url = f"{base_url}?route=api/sale/customer&api_token={get_api_token}"

    try:
        payload = AddCustomerRequest(**test_data.user_data)
    except ValidationError as e:
        logger.error(f"Data validation failed: {e}")

    headers = {}

    logger.info(f"Sending request {get_api_token}")
    response = requests.request("POST", target_url, headers=headers, data=payload.model_dump(), verify=False)
    logger.info(f"response from server: \n {response.json()}")

    logger.info(f"Getting session {get_api_token} data from DB")
    # session_data_raw = db_models_and_session.execute(text("SELECT data FROM oc_session WHERE session_id = :session_id"),
    #                                                  {"session_id": get_api_token}).scalar()
    # logger.info(f"From session {get_api_token} have got data {session_data_raw}")
    session = models["oc_session"]
    session_data_raw = db_session.query(session.data).filter(session.session_id == get_api_token).scalar()
    session_data = json.loads(session_data_raw)

    assert ((session_data['customer']['customer_group_id'] == test_data.user_data['customer_group_id']) and
            (session_data['customer']['firstname'] == test_data.user_data['firstname']) and
            (session_data['customer']['lastname'] == test_data.user_data['lastname']) and
            (session_data['customer']['email'] == test_data.user_data['email']))
