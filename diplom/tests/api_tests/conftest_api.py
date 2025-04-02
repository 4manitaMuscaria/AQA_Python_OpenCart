import pytest
from sqlalchemy import text
from diplom.config.credentials import Credetntials


def pytest_addoption(parser):
    parser.addoption(
        "--api_url",
        default=f"https://{Credetntials.HOST}/index.php",
        help="This is request url"
    )


@pytest.fixture()
def base_url(request):
    return request.config.getoption("--api_url")


@pytest.fixture()
def api_setup(logger, db_session):

    api_ip = db_session.execute(text("SELECT * FROM oc_api_ip WHERE ip = :ip"),
                                {"ip": "172.18.0.1"}).fetchone()
    logger.info(f"найден ip {api_ip}")

    if not api_ip:
        db_session.execute(text("INSERT INTO oc_api_ip (api_ip_id, api_id, ip) VALUES (:api_ip_id, :api_id, :ip)"),
                           {"api_ip_id": 1,
                            "api_id": 1,
                            "ip": "172.18.0.1"})
        db_session.commit()

    key = db_session.execute(text("SELECT `key` FROM oc_api WHERE username = :username"),
                             {"username": Credetntials.API_CREDS["username"]}).scalar()
    logger.info(f"получили ключ {key}")

    yield key
