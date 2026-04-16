import allure

from api.ad_api import AdMethods
from assertions.assertions import assert_ad_response_structure
from data import Data


@allure.feature("Создание объявления")
class TestCreateAd:

    @allure.title("Успешное создание объявления со случайной категорией")
    def test_create_ad(self, get_access_token, random_category_in_request_create_ad):
        response = AdMethods().create_ad(
            random_category_in_request_create_ad, get_access_token
        )

        assert response.status_code == Data.CREATE_AD_CODE, (
            f"Ожидается {Data.CREATE_AD_CODE}, получен {response.status_code}"
        )

        assert_ad_response_structure(response.json())