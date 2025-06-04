import json
import requests
import allure
import pytest

from pydantic import ValidationError
from OpenCart_autotests.models import AddVoucherRequest, AddVoucherResponse


@allure.epic('API тесты')
@allure.story('Добавление ваучера')
@allure.title('Проверка статуса')
def test_add_voucher_status(logger, base_url, get_api_token, test_data, delete_session):
    target_url = f"{base_url}?route=api/sale/voucher.add&api_token={get_api_token}"

    try:
        payload = AddVoucherRequest(**test_data.voucher_data)
    except ValidationError as e:
        logger.error(f"Data validation failed: {e}")

    headers = {}

    logger.info("Sending request")
    response = requests.request("POST", target_url, headers=headers, data=payload.model_dump(), verify=False)
    assert response.status_code == 200


@allure.epic('API тесты')
@allure.story('Добавление ваучера')
@allure.title('Валидация ответа')
def test_add_voucher_validate(logger, base_url, get_api_token, test_data, delete_session):
    target_url = f"{base_url}?route=api/sale/voucher.add&api_token={get_api_token}"

    try:
        payload = AddVoucherRequest(**test_data.voucher_data)
    except ValidationError as e:
        logger.error(f"Data validation failed: {e}")

    headers = {}

    logger.info("Sending request")
    response = requests.request("POST", target_url, headers=headers, data=payload.model_dump(), verify=False).json()

    logger.info("Validating response")
    try:
        validated_data = AddVoucherResponse(**response)
        assert isinstance(validated_data, AddVoucherResponse), "Ответ не валиден по схеме AddVoucherResponse"
    except ValidationError as e:
        pytest.fail(f"Ошибка валидации {e.json()}")


@allure.epic('API тесты')
@allure.story('Добавление ваучера')
@allure.title('Проверка сохраненных данных')
def test_add_voucher_data(logger, models, db_session, base_url, get_api_token, test_data, delete_session):
    target_url = f"{base_url}?route=api/sale/voucher.add&api_token={get_api_token}"

    try:
        payload = AddVoucherRequest(**test_data.voucher_data)
    except ValidationError as e:
        logger.error(f"Data validation failed: {e}")

    headers = {}

    logger.info("Sending request")
    requests.request("POST", target_url, headers=headers, data=payload.model_dump(), verify=False)

    logger.info(f"Getting session {get_api_token} data from DB")
    # session_data_raw = db_models_and_session.execute(text("SELECT data FROM oc_session WHERE session_id = :session_id"),
    #                                                  {"session_id": get_api_token}).scalar()
    session = models["oc_session"]
    session_data_raw = db_session.query(session.data).filter(session.session_id == get_api_token).scalar()
    session_data = json.loads(session_data_raw)

    assert ((session_data['vouchers'][0]['to_name'] == test_data.voucher_data['to_name']) and
            (session_data['vouchers'][0]['to_email'] == test_data.voucher_data['to_email']) and
            (session_data['vouchers'][0]['from_name'] == test_data.voucher_data['from_name']) and
            (session_data['vouchers'][0]['from_email'] == test_data.voucher_data['from_email']) and
            (session_data['vouchers'][0]['voucher_theme_id'] == test_data.voucher_data['voucher_theme_id']) and
            (session_data['vouchers'][0]['message'] == test_data.voucher_data['message']) and
            (str(session_data['vouchers'][0]['amount']) == test_data.voucher_data['amount']))
