from dataclasses import dataclass
import pytest
from httpx import AsyncClient

from app.settings import Settings
from app.users.auth.schema import GoogleUserData, YandexUserData
from faker import Factory as FakerFactory

from tests.fixtures.users.user_model import EXISTS_GOOGLE_USER_EMAIL, EXISTS_GOOGLE_USER_ID

faker = FakerFactory.create()

@dataclass
class FakeGoogleClient:
    settings: Settings
    async_client: AsyncClient

    async def get_user_info(self, code: str)-> GoogleUserData:
        access_token = await self._get_user_access_token(code=code)
        return google_user_info_date()

    async def _get_user_access_token(self, code: str)->str:
        return f"fake_access_token_{code}"

@dataclass
class FakeYandexClient:
    settings: Settings
    async_client: AsyncClient

    async def get_user_info(self, code: str)-> YandexUserData:
        access_token = await self._get_user_access_token(code=code)
        return yandex_user_info_date()

    async def _get_user_access_token(self, code: str)->str:
        return f"fake_access_token_{code}"


@pytest.fixture
def google_client():
    return FakeGoogleClient(settings=Settings(), async_client=AsyncClient())

@pytest.fixture
def yandex_client():
    return FakeYandexClient(settings=Settings(), async_client=AsyncClient())


def google_user_info_date()->GoogleUserData:
    return GoogleUserData(
        id=EXISTS_GOOGLE_USER_ID,#faker.random_int(),
        email=EXISTS_GOOGLE_USER_EMAIL, #faker.email(),
        name=faker.name(),
        verified_email=True,
        access_token=faker.sha256(),
    )

def yandex_user_info_date()->YandexUserData:
    return YandexUserData(
        id=faker.random_int(),
        login=faker.name(),
        default_email=faker.email(),
        real_name=faker.name(),
        access_token=faker.sha256(),
    )
