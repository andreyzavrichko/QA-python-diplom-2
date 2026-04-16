import allure

from api.user_api import RegisterUser
from data import Data


@allure.feature("Регистрация пользователя")
class TestRegisterUser:

    @allure.title("Успешная регистрация нового пользователя")
    def test_create_user(self):
        response = RegisterUser().register_user_and_return_response()

        assert response.status_code == Data.REGISTER_RESP_CODE, (
            f"Ожидается {Data.REGISTER_RESP_CODE}, получен {response.status_code}"
        )

        data = response.json()

        assert "user" in data
        assert "access_token" in data

    @allure.title("Повторная регистрация существующего пользователя возвращает 400")
    def test_register_user_already_exist(self):
        response = RegisterUser().register_user_already_exist()

        assert response.status_code == Data.REGISTER_ALREADY_EXIST_CODE, (
            f"Ожидается {Data.REGISTER_ALREADY_EXIST_CODE}, получен {response.status_code}"
        )
        assert response.text == Data.REGISTER_USER_ALREADY_EXIST_RESPONSE_BODY, (
            f"Тело ответа не совпадает: {response.text}"
        )
