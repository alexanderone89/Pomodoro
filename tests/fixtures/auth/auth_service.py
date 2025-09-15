import pytest_asyncio

from app.settings import Settings
from app.users.auth.service import AuthService
from app.users.user_profile.repository import UserRepository
from tests.fixtures.auth.clients import google_client, yandex_client
from tests.fixtures.users.user_repository import fake_user_repository




@pytest_asyncio.fixture(autouse=True, scope="function")
# @pytest_asyncio.fixture(autouse=True, scope="session")
def mock_auth_service(
        yandex_client,
        google_client,
        fake_user_repository
):
    return AuthService(
        user_repository=fake_user_repository,
        settings=Settings(),
        google_client=google_client,
        yandex_client=yandex_client
    )


@pytest_asyncio.fixture(autouse=True, scope="function")
# @pytest_asyncio.fixture(autouse=True, scope="session")
def auth_service(
        yandex_client,
        google_client,
        mock_auth_service,
        get_db_session,
):
    return AuthService(
        user_repository=UserRepository(db_session=get_db_session),
        settings=Settings(),
        google_client=google_client,
        yandex_client=yandex_client,
)