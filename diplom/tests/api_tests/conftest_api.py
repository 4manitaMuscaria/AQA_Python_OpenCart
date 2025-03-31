import pytest
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


