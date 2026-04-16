import allure

from api.ad_api import AdMethods
from assertions.assertions import assert_ad_response_structure
from data import Data


@allure.feature("Редактирование объявления")
class TestUpdateAd:

    @allure.title("Успешное редактирование своего объявления")
    def test_update_ad(self, get_access_token):
        payload = Data.CREATE_AD_REQUEST_BODY.copy()
        original_name = payload["name"]

        response = AdMethods().update_ad(payload, get_access_token)

        assert response.status_code == Data.UPDATE_AD_CODE, (
            f"Ожидается {Data.UPDATE_AD_CODE}, получен {response.status_code}"
        )

        data = response.json()
        assert data["name"] != original_name, "Название объявления не изменилось"
        assert_ad_response_structure(data)

    @allure.title("Редактирование чужого объявления возвращает 401")
    def test_update_foreign_ad(self, get_access_token):
        response = AdMethods().update_foreign_ad(get_access_token)

        assert response.status_code == Data.UPDATE_FOREIGN_AD_CODE, (
            f"Ожидается {Data.UPDATE_FOREIGN_AD_CODE}, получен {response.status_code}"
        )
        assert response.json() == Data.UPDATE_FOREIGN_AD_RESPONSE_BODY_401, (
            f"Тело ответа не совпадает: {response.json()}"
        )
