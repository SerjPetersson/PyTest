import pytest
import requests
from configuration import SERVICE_URL1


@pytest.fixture
def get_users():
    response = requests.get(SERVICE_URL1)
    return response
