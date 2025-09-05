import pytest

from app.settings import Settings
from app.users.auth.service import AuthService
from tests.fixtures.auth.clients import google_client, yandex_client
from tests.fixtures.users.user_repository import user_repository

@pytest.fixture
def auth_service(yandex_client,google_client,user_repository):
    return AuthService(
        user_repository=user_repository,
        settings=Settings(),
        google_client=google_client,
        yandex_client=yandex_client
    )
