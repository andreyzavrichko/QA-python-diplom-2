import allure
import requests

from data import Data
from helpers import make_register_data


class RegisterUser:
    @allure.step("Регистрация нового пользователя")
    def register_user_and_return_response(self):
        payload = make_register_data()
        response = requests.post(Data.BASE_URL + Data.REGISTER_URL, data=payload)
        return response

    @allure.step("Повторная регистрация существующего пользователя")
    def register_user_already_exist(self):
        payload = {
            "email": Data.EXISTING_USER_EMAIL,
            "password": Data.EXISTING_USER_PASSWORD,
            "submitPassword": Data.EXISTING_USER_PASSWORD,
        }
        return requests.post(Data.BASE_URL + Data.REGISTER_URL, json=payload)


class AuthUser:
    @allure.step("Авторизация пользователя")
    def auth_user(self, payload: dict):
        response = requests.post(Data.BASE_URL + Data.AUTH_URL, data=payload)
        return response