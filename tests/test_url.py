import requests
from configuration import SERVICE_URL1
from src.basedclasses.response import Response
from src.schemas.users import User


def test_get_users():
    response = requests.get(SERVICE_URL1)
    test_objects = Response(response)
    test_objects.assert_status_code(200).validate(User)

