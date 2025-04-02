import pytest
import requests

from sqlalchemy import text
from diplom.config.credentials import Credetntials


@pytest.fixture()
def get_api_token(logger, base_url, api_setup):
    logger.info("Getting API-token")

    target_url = f"{base_url}?route=api/account/login"
    logger.info(f"из фикстуры получен ключ {api_setup}")
    payload = f'username={Credetntials.API_CREDS["username"]}&key={Credetntials.API_CREDS["key"]}'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", target_url, headers=headers, data=payload, verify=False)
    logger.info(payload, response.json())

    yield response.json()['api_token']


@pytest.fixture()
def delete_session(logger, db_session, get_api_token):

    yield

    logger.info(f"Deleting session {get_api_token} from database...")
    db_session.execute(text("DELETE FROM oc_session WHERE session_id = :session_id"),
                       {"session_id": get_api_token})
    db_session.commit()


@pytest.fixture()
def add_voucher(logger, base_url, get_api_token, test_data):
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

    logger.info("Sending request to add voucher")
    requests.request("POST", target_url, headers=headers, data=payload, verify=False)
