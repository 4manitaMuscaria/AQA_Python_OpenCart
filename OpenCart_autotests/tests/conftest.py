import pytest
import os
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import MetaData
from sqlalchemy.orm import relationship
from OpenCart_autotests.utils.logger import LoggerManager
from OpenCart_autotests.config.credentials import Credentials

pytest_plugins = [
    "OpenCart_autotests.tests.ui_tests.conftest_ui",
    "OpenCart_autotests.tests.ui_tests.fixtures_ui",
    "OpenCart_autotests.tests.api_tests.conftest_api",
    "OpenCart_autotests.tests.api_tests.fixtures_api"
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
def db_models_and_session(logger):
    """
    Фикстура для работы с базой данных
    """
    logger.info("DB connection")
    engine = create_engine(f"mysql+pymysql://{Credentials.DB_CREDS['user']}:{Credentials.DB_CREDS['password']}@"
                           f"{Credentials.HOST}:{Credentials.DB_CREDS['port']}/"
                           f"{Credentials.DB_CREDS['db_name']}",
                           isolation_level="READ COMMITTED")
    logger.info("Connecting DB and opening session")
    connection = engine.connect()
    # transaction = connection.begin()

    logger.info("Creating models")

    # Создаем метаданные только для нужных таблиц
    metadata = MetaData()
    selected_tables = [
        "oc_customer",
        "oc_address",
        "oc_category",
        "oc_category_description",
        "oc_seo_url",
        "oc_api",
        "oc_api_ip",
        "oc_session",
        "oc_upload"
    ]

    # Загружаем только указанные таблицы
    metadata.reflect(engine, only=selected_tables)

    # Генерируем модели только для этих таблиц
    base = automap_base(metadata=metadata)
    base.prepare()

    # Собираем модели в словарь
    models = {
        table_name: getattr(base.classes, table_name)
        for table_name in selected_tables
    }

    logger.info("Session opening")

    Session = sessionmaker(bind=connection)
    session = Session()

    try:
        yield {"models": models, "session": session}
    finally:
        # transaction.rollback()
        connection.close()
        session.close()
        logger.info("Session closed")


@pytest.fixture(scope="function")
def db_session(db_models_and_session):
    yield db_models_and_session["session"]


@pytest.fixture(scope="function")
def models(db_models_and_session):
    yield db_models_and_session["models"]
