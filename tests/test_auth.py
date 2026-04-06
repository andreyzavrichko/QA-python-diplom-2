import allure

from api.user_api import AuthUser
from data import Data


@allure.feature("Авторизация пользователя")
class TestAuthUser:

    @allure.title("Успешная авторизация зарегистрированного пользователя")
    def test_auth_user(self):
        response = AuthUser().auth_user(Data.USER_LOGIN_DATA)

        assert response.status_code == Data.AUTH_CODE, (
            f"Ожидается {Data.AUTH_CODE}, получен {response.status_code}"
        )

        data = response.json()

        assert "user" in data
        assert "token" in data
