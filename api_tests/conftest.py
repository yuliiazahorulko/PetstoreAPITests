import pytest
from api_tests.api_client import PetstoreAPIClient

@pytest.fixture(scope="module")
def api_client():
    return PetstoreAPIClient()
