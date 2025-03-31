import pytest
import os
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from diplom.utils.logger import LoggerManager
from diplom.config.credentials import Credetntials


pytest_plugins = [
    "diplom.tests.ui_tests.conftest_ui",
    "diplom.tests.ui_tests.fixtures_ui",
    "diplom.tests.api_tests.conftest_api",
    "diplom.tests.api_tests.fixtures_api"
]


def pytest_addoption(parser):
    parser.addoption("--log_level", action="store", default="INFO")


@pytest.fixture(scope="function")
def logger(request):
    """
    Фикстура создает файл с логами
    :param request:
    :return:
    """

    # Создаем папку и файл с логами
    test_name = request.session.items[0].name
    # print(f"DEBUG: test_name before cleaning: {test_name}")
    log_directory = "logs"
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    log_filename = f"{test_name}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
    log_path = os.path.join(log_directory, log_filename)

    log_level = request.config.getoption("--log_level")

    # Создаем логгер
    logger = LoggerManager.get_logger(log_level=log_level, log_to_file=True, log_path=log_path, log_name=test_name)

    yield logger


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call":
        # Получаем фикстуру logger из аргументов теста
        logger = LoggerManager.get_logger()

        if rep.outcome != 'passed':
            status = 'failed'
            logger.error(f"Тест '{item.name}' завершился с ошибкой:\n{rep.longrepr}", exc_info=True)
        else:
            status = 'passed'
        item.funcargs["test_status"] = status


@pytest.fixture(scope="function")
def db_session(logger):
    """
    Фикстура для работы с базой данных в рамках транзакции.
    """
    engine = create_engine(f"mysql+pymysql://{Credetntials.DB_CREDS['user']}:{Credetntials.DB_CREDS['password']}@"
                           f"{Credetntials.HOST}:{Credetntials.DB_CREDS['port']}/"
                           f"{Credetntials.DB_CREDS['db_name']}")
    logger.info("Connecting DB and opening session")
    connection = engine.connect()
    # transaction = connection.begin()

    Session = sessionmaker(bind=connection)
    session = Session()

    try:
        yield session
    finally:
        # transaction.rollback()
        connection.close()
        session.close()
