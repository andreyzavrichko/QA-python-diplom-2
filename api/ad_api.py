import allure
import requests

from pathlib import Path

from data import Data

IMAGE_PATH = Path(__file__).parent.parent / "tests" / "files" / "garage.jpg"


class AdMethods:
    @allure.step("Создание объявления")
    def create_ad(self, payload: dict, header: dict):
        payload = payload.copy()
        headers = header.copy()

        with open(IMAGE_PATH, "rb") as f:
            files = {
                "images": ("garage.jpg", f, "image/jpeg")
            }

            response = requests.post(
                Data.BASE_URL + Data.CREATE_AD_URL,
                headers=headers,
                data=payload,
                files=files
            )
        return response

    @allure.step("Редактирование своего объявления")
    def update_ad(self, payload: dict, header: dict):
        response_create = self.create_ad(payload, header)
        id_ad = response_create.json()["id"]
        payload = payload.copy()
        payload["name"] = payload["name"] + " (изменено)"
        update_url = f"{Data.BASE_URL}{Data.UPDATE_AD_URL}{id_ad}"
        response = requests.patch(update_url, headers=header, data=payload)
        return response

    @allure.step("Редактирование чужого объявления")
    def update_foreign_ad(self, header: dict):
        listing_response = requests.get(Data.BASE_URL + Data.LISTING_URL, headers=header)
        foreign_ad = listing_response.json()["offers"][0]
        id_foreign_ad = foreign_ad["id"]
        payload = {"name": foreign_ad["name"] + " (изменено)"}
        url = f"{Data.BASE_URL}{Data.UPDATE_AD_URL}{id_foreign_ad}"
        response = requests.patch(url, headers=header, data=payload)
        return response

    @allure.step("Удаление объявления")
    def delete_ad(self, header: dict):
        payload = Data.CREATE_AD_REQUEST_BODY.copy()
        response_create = self.create_ad(payload, header)
        id_ad = response_create.json()["id"]
        url = f"{Data.BASE_URL}{Data.DELETE_URL}{id_ad}"
        response = requests.delete(url, headers=header)
        return response