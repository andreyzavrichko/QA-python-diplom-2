import random
import pytest

from api.user_api import AuthUser
from data import Data


@pytest.fixture()
def get_access_token() -> dict:
    response = AuthUser().auth_user(Data.USER_LOGIN_DATA)
    token = response.json()["token"]["access_token"]
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture()
def random_category_in_request_create_ad() -> dict:
    payload = Data.CREATE_AD_REQUEST_BODY.copy()
    payload["category"] = random.choice(Data.CATEGORY_LIST)
    return payload