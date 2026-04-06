from http import HTTPStatus


class Data:
    BASE_URL = "https://qa-desk.stand.praktikum-services.ru/api/"

    REGISTER_URL = "signup"
    AUTH_URL = "signin"
    CREATE_AD_URL = "create-listing"
    UPDATE_AD_URL = "update-offer/"
    LISTING_URL = "listings/1"
    DELETE_URL = "listings/"

    REGISTER_RESP_CODE = HTTPStatus.CREATED
    REGISTER_ALREADY_EXIST_CODE = HTTPStatus.BAD_REQUEST
    AUTH_CODE = HTTPStatus.CREATED
    CREATE_AD_CODE = HTTPStatus.CREATED
    UPDATE_AD_CODE = HTTPStatus.OK
    UPDATE_FOREIGN_AD_CODE = HTTPStatus.UNAUTHORIZED
    DELETE_AD_CODE = HTTPStatus.OK

    EXISTING_USER_EMAIL = "test12@test.test"
    EXISTING_USER_PASSWORD = "123456"

    REGISTER_USER_ALREADY_EXIST = (
        '{"email": "test12@test.test", "password": "123456", "submitPassword": "123456"}'
    )
    REGISTER_USER_ALREADY_EXIST_RESPONSE_BODY = (
        '{"statusCode":400,"message":"Почта уже используется"}'
    )

    USER_LOGIN_DATA = {
        "email": EXISTING_USER_EMAIL,
        "password": EXISTING_USER_PASSWORD,
    }

    CREATE_AD_REQUEST_BODY = {
        "name": "Продам гараж",
        "category": "Технологии",
        "condition": "Б/У",
        "city": "Москва",
        "description": (
            "Продам гараж"
        ),
        "price": "1500",
        "images": None,
    }

    CATEGORY_LIST = ["Авто", "Садоводство", "Хобби", "Книги", "Технологии"]

    UPDATE_FOREIGN_AD_RESPONSE_BODY_401 = {
        "error": "Unauthorized",
        "message": "Оффер не найден или у вас нет прав на его редактирование",
        "statusCode": 401,
    }
    DELETE_AD_RESPONSE = {"message": "Объявление удалено успешно"}
