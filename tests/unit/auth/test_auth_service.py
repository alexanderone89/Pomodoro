import pytest
from jose import jwt
import datetime as dt

from twisted.application.strports import service

from app.settings import Settings
from app.users.auth.client import GoogleClient
from app.users.auth.schema import UserLoginSchema
# from app.settings import Settings


from app.users.auth.service import AuthService
from app.users.user_profile.models import UserProfile

pytestmark = pytest.mark.asyncio

async def test_get_google_redirect_url__success(auth_service: AuthService, settings: Settings):
    auth_service_google_redirect_url = auth_service.get_google_redirect_url()

    settings_google_redirect_url = settings.google_redirect_url

    assert settings_google_redirect_url == auth_service_google_redirect_url

async def test_get_yandex_redirect_url__success(auth_service: AuthService, settings: Settings):
    auth_service_yandex_redirect_url = auth_service.get_yandex_redirect_url()

    settings_yandex_redirect_url = settings.yandex_redirect_url

    assert settings_yandex_redirect_url == auth_service_yandex_redirect_url


async def test_get_google_redirect_url__fail(auth_service: AuthService):
    settings_google_redirect_url = "https://fake_google.com"

    auth_service_google_redirect_url = auth_service.get_google_redirect_url()

    assert auth_service_google_redirect_url != settings_google_redirect_url

async def test_generate_access_token__success(auth_service: AuthService, settings: Settings):
    user_id = str(1)

    access_token = auth_service.generate_access_token(user_id=user_id)
    decode_access_token = jwt.decode(access_token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ENCODE_ALGORITHM])
    decode_user_id = decode_access_token.get("user_id")
    decode_token_expire = dt.datetime.fromtimestamp(decode_access_token.get("exp"), tz=dt.timezone.utc)

    # dt.UTC
    assert (decode_token_expire - dt.datetime.now(tz=dt.timezone.utc)) > dt.timedelta(days=6)
    assert decode_user_id == user_id


async def test_get_user_id_from_token__success(auth_service: AuthService):
    user_id = str(1)

    access_token = auth_service.generate_access_token(user_id=user_id)
    decode_user_id = auth_service.get_user_id_from_access_token(access_token)

    assert decode_user_id == user_id


async def test_google_auth__success(auth_service: AuthService):
    code = "fake_code"


    user = await auth_service.google_auth(code=code)
    decoded_user_id = auth_service.get_user_id_from_access_token(user.access_token)

    assert decoded_user_id == user.user_id
    assert isinstance(user, UserLoginSchema)


async def test_yandex_auth__success(auth_service: AuthService):
    code = "fake_code"

    user = await auth_service.yandex_auth(code=code)
    decoded_user_id = auth_service.get_user_id_from_access_token(user.access_token)

    assert user.user_id == decoded_user_id
    assert isinstance(user, UserLoginSchema)
