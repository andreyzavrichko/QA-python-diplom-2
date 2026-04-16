import allure

from api.ad_api import AdMethods
from data import Data


@allure.feature("Удаление объявления")
class TestDeleteAd:

    @allure.title("Успешное удаление своего объявления")
    def test_delete_ad(self, get_access_token):
        response = AdMethods().delete_ad(get_access_token)

        assert response.status_code == Data.DELETE_AD_CODE, (
            f"Ожидается {Data.DELETE_AD_CODE}, получен {response.status_code}"
        )
        assert response.json() == Data.DELETE_AD_RESPONSE, (
            f"Тело ответа не совпадает: {response.json()}"
        )