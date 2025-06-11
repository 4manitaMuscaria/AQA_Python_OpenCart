import pytest
from sqlalchemy import text
from OpenCart_autotests.config.credentials import Credentials


def pytest_addoption(parser):
    parser.addoption(
        "--api_url",
        default=f"https://{Credentials.HOST}/index.php",
        help="This is request url"
    )


@pytest.fixture()
def base_url(request):
    return request.config.getoption("--api_url")


@pytest.fixture()
def api_setup(logger, models, db_session):
    # api_ip = db_models_and_session.execute(text("SELECT * FROM oc_api_ip WHERE ip = :ip"),
    #                                        {"ip": "172.18.0.1"}).fetchone()
    ApiIp = models["oc_api_ip"]
    api_ip = db_session.query(ApiIp).filter(ApiIp.ip == "172.18.0.1").first()

    if not api_ip:
        # db_models_and_session.execute(text("INSERT INTO oc_api_ip (api_ip_id, api_id, ip) VALUES (:api_ip_id, :api_id, :ip)"),
        #                               {"api_ip_id": 1,
        #                     "api_id": 1,
        #                     "ip": "172.18.0.1"})
        db_session.add(ApiIp(api_ip_id=1, api_id=1, ip="172.18.0.1"))
        db_session.commit()
        logger.info(f"Добавляем IP 172.18.0.1 в список, если он не найден")

    Api = models["oc_api"]
    # api_key = db_models_and_session.execute(text("SELECT `key` FROM oc_api WHERE username = :username"),
    #                                         {"username": Credetntials.API_CREDS["username"]}).scalar()
    api_key = db_session.query(Api.key).filter(Api.username == Credentials.API_CREDS["username"]).scalar()

    return api_key

