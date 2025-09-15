import asyncio
import pytest
from pytest_asyncio import is_async_test


pytest_plugins = [
    "tests.fixtures.auth.auth_service",
    "tests.fixtures.auth.clients",
    "tests.fixtures.users.user_repository",
    "tests.fixtures.infrastructure",
    "tests.fixtures.users.user_model",
]


def pytest_collection_modifyitems(items):
    pytest_asyncio_tests = (item for item in items if is_async_test(item))
    session_scope_marker = pytest.mark.asyncio(loop_scope="session")
    for async_test in pytest_asyncio_tests:
        async_test.add_marker(session_scope_marker, append=False)


@pytest.fixture(scope='session')
def event_loop():
    loop = asyncio.get_event_loop()
    # if loop.is_closed():
    #     loop = asyncio.new_event_loop()
    yield loop
    # loop.close()

    # loop = asyncio.get_event_loop_policy().new_event_loop()
    # yield loop
    # loop.close()

    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    # yield loop
    # loop.close()

    # policy = asyncio.get_event_loop_policy()
    # loop = policy.new_event_loop()
    # yield loop
    # loop.close()

    # try:
    #     loop = asyncio.get_running_loop()
    # except RuntimeError:
    #     loop = asyncio.new_event_loop()
    # yield loop
    # loop.close()


