import json
import requests
import allure
import pytest

from pydantic import ValidationError
from sqlalchemy import text
from diplom.models.add_voucher_response_model import AddVoucherResponse


@allure.epic('API тесты')
@allure.story('Добавление ваучера')
@allure.title('Проверка статуса')
def test_add_voucher_status(logger, db_session, base_url, get_api_token, test_data, delete_session):
    target_url = f"{base_url}?route=api/sale/voucher.add&api_token={get_api_token}"

    payload = {'from_name': test_data.voucher_data['from_name'],
               'from_email': test_data.voucher_data['from_email'],
               'to_name': test_data.voucher_data['to_name'],
               'to_email': test_data.voucher_data['to_email'],
               'voucher_theme_id': test_data.voucher_data['voucher_theme_id'],
               'message': test_data.voucher_data['message'],
               'amount': test_data.voucher_data['amount']}

    headers = {
        'Cookie': 'OCSESSID=a10f1082cb2db0e5b4aab9f8ab; currency=USD'
    }

    logger.info("Sending request")
    response = requests.request("POST", target_url, headers=headers, data=payload, verify=False)
    assert response.status_code == 200


@allure.epic('API тесты')
@allure.story('Добавление ваучера')
@allure.title('Валидация ответа')
def test_add_voucher_validate(logger, db_session, base_url, get_api_token, test_data, delete_session):
    target_url = f"{base_url}?route=api/sale/voucher.add&api_token={get_api_token}"

    payload = {'from_name': test_data.voucher_data['from_name'],
               'from_email': test_data.voucher_data['from_email'],
               'to_name': test_data.voucher_data['to_name'],
               'to_email': test_data.voucher_data['to_email'],
               'voucher_theme_id': test_data.voucher_data['voucher_theme_id'],
               'message': test_data.voucher_data['message'],
               'amount': test_data.voucher_data['amount']}

    headers = {
        'Cookie': 'OCSESSID=a10f1082cb2db0e5b4aab9f8ab; currency=USD'
    }

    logger.info("Sending request")
    response = requests.request("POST", target_url, headers=headers, data=payload, verify=False).json()

    logger.info("Validating response")
    try:
        validated_data = AddVoucherResponse(**response)
        assert isinstance(validated_data, AddVoucherResponse), "Ответ не валиден по схеме AddVoucherResponse"
    except ValidationError as e:
        pytest.fail(f"Ошибка валидации {e.json()}")


@allure.epic('API тесты')
@allure.story('Добавление ваучера')
@allure.title('Проверка сохраненных данных')
def test_add_voucher_data(logger, db_session, base_url, get_api_token, test_data, delete_session):
    target_url = f"{base_url}?route=api/sale/voucher.add&api_token={get_api_token}"

    payload = {'from_name': test_data.voucher_data['from_name'],
               'from_email': test_data.voucher_data['from_email'],
               'to_name': test_data.voucher_data['to_name'],
               'to_email': test_data.voucher_data['to_email'],
               'voucher_theme_id': test_data.voucher_data['voucher_theme_id'],
               'message': test_data.voucher_data['message'],
               'amount': test_data.voucher_data['amount']}

    headers = {
        'Cookie': 'OCSESSID=a10f1082cb2db0e5b4aab9f8ab; currency=USD'
    }

    logger.info("Sending request")
    requests.request("POST", target_url, headers=headers, data=payload, verify=False)

    logger.info(f"Getting session {get_api_token} data from DB")
    session_data_raw = db_session.execute(text("SELECT data FROM oc_session WHERE session_id = :session_id"),
                                          {"session_id": get_api_token}).scalar()
    session_data = json.loads(session_data_raw)

    assert ((session_data['vouchers'][0]['to_name'] == test_data.voucher_data['to_name']) and
            (session_data['vouchers'][0]['to_email'] == test_data.voucher_data['to_email']) and
            (session_data['vouchers'][0]['from_name'] == test_data.voucher_data['from_name']) and
            (session_data['vouchers'][0]['from_email'] == test_data.voucher_data['from_email']) and
            (session_data['vouchers'][0]['voucher_theme_id'] == test_data.voucher_data['voucher_theme_id']) and
            (session_data['vouchers'][0]['message'] == test_data.voucher_data['message']) and
            (str(session_data['vouchers'][0]['amount']) == test_data.voucher_data['amount']))
