import re
from types import NoneType

import allure


@allure.step("Проверка структуры и типов ответа объявления")
def assert_ad_response_structure(data: dict) -> None:
    """Проверяет наличие ключей и типы данных в ответе объявления."""
    assert "category" in data
    assert "city" in data
    assert "condition" in data
    assert "description" in data
    assert "img1" in data
    assert "img2" in data
    assert "img3" in data
    assert "isFavorite" in data
    assert "name" in data
    assert "createdAt" in data
    assert "updatedAt" in data
    assert "owner" in data
    assert "id" in data
    assert "price" in data

    assert isinstance(data["category"], str)
    assert isinstance(data["city"], str)
    assert isinstance(data["condition"], str)
    assert isinstance(data["description"], str)
    assert isinstance(data["img1"], str)
    assert isinstance(data["img2"], NoneType)
    assert isinstance(data["img3"], NoneType)
    assert isinstance(data["isFavorite"], NoneType)
    assert isinstance(data["name"], str)
    assert isinstance(data["owner"], int)
    assert isinstance(data["price"], int)
    assert isinstance(data["id"], int)
    assert isinstance(data["createdAt"], str)
    assert isinstance(data["updatedAt"], str)


@allure.step("Проверка JWT-токена")
def assert_jwt_token(token: str) -> None:
    """Проверяет, что строка является валидным JWT (три части base64url)."""
    parts = token.split(".")
    assert len(parts) == 3, "Токен не является JWT: ожидается три части через точку"
    assert re.match(r"^[A-Za-z0-9\-_]+$", parts[0]), "Заголовок JWT содержит недопустимые символы"
    assert re.match(r"^[A-Za-z0-9\-_]+$", parts[1]), "Payload JWT содержит недопустимые символы"
    assert re.match(r"^[A-Za-z0-9\-_]+$", parts[2]), "Подпись JWT содержит недопустимые символы"