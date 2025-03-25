import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--api_url",
        default="https://192.168.149.196/index.php",
        help="This is request url"
    )


@pytest.fixture()
def base_url(request):
    return request.config.getoption("--api_url")


