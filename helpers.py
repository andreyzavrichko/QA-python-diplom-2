from faker import Faker

_fake = Faker()


def make_register_data() -> dict:
    return {
        "email": _fake.unique.email(),
        "password": "Pa$$Word123",
        "submitPassword": "Pa$$Word123",
    }