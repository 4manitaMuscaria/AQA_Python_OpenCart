import json
import requests
import allure
import pytest

from pydantic import ValidationError
from OpenCart_autotests.models import (GetAvailableRewardResponse, GetMaximumRewardResponse, PostRewardRequest,
                                       PostRewardSuccessResponse, PostRewardErrorResponse)


@allure.epic('API тесты')
@allure.story('Проверки бонусных баллов')
@allure.title('Проверка списания баллов')
@pytest.mark.parametrize("reward, model",
                         [("0", PostRewardSuccessResponse),
                          ("50", PostRewardErrorResponse)])
def test_post_reward(logger, base_url, get_api_token, delete_session, reward, model):
    target_url = f"{base_url}?route=api/sale/reward&api_token={get_api_token}"

    try:
        payload = PostRewardRequest(reward=reward)
    except ValidationError as e:
        logger.error(f"Data validation failed: {e}")

    headers = {}

    logger.info("Sending request")
    response = requests.request("POST", target_url, headers=headers, data=payload.model_dump(), verify=False)

    # Проверка статуса
    assert response.status_code == 200

    # Валидация ответа
    logger.info("Validating response")
    try:
        validated_data = model(**response.json())
        assert isinstance(validated_data, model), "Ответ не валиден по схеме AddVoucherResponse"
    except ValidationError as e:
        pytest.fail(f"Ошибка валидации {e.json()}")

@allure.epic('API тесты')
@allure.story('Проверки бонусных баллов')
@allure.title('Проверка максимума баллов')
def test_get_maximum_reward(logger, base_url, get_api_token, delete_session):
    target_url = f"{base_url}?route=api/sale/reward.maximum&api_token={get_api_token}"

    payload = {}
    headers = {}

    logger.info("Sending request")
    response = requests.request("GET", target_url, headers=headers, data=payload, verify=False)

    # Проверка статуса
    assert response.status_code == 200

    # Валидация ответа
    logger.info("Validating response")
    try:
        validated_data = GetMaximumRewardResponse(**response.json())
        assert isinstance(validated_data, GetMaximumRewardResponse)
    except ValidationError as e:
        pytest.fail(f"Validation failed: {e}")


@allure.epic('API тесты')
@allure.story('Проверки бонусных баллов')
@allure.title('Проверка доступных баллов')
def test_get_available_reward(logger, base_url, get_api_token, delete_session):
    target_url = f"{base_url}?route=api/sale/reward.available&api_token={get_api_token}"

    payload = {}
    headers = {}

    logger.info("Sending request")
    response = requests.request("GET", target_url, headers=headers, data=payload, verify=False)

    # Проверка статуса
    assert response.status_code == 200

    # Валидация ответа
    logger.info("Validating response")
    try:
        validated_data = GetAvailableRewardResponse(**response.json())
        assert isinstance(validated_data, GetAvailableRewardResponse)
    except ValidationError as e:
        pytest.fail(f"Validation failed: {e}")