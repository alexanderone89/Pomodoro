import pytest
import pytest_asyncio
from sqlalchemy import StaticPool, NullPool
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from app.infrastructure.database.database import Base
from app.settings import Settings


@pytest.fixture
def settings():
    return Settings()


engine = create_async_engine(
    url="postgresql+asyncpg://postgres:password@127.0.0.1:5432/pomodoro-test",
    future=True,
    echo=True,
    pool_pre_ping=True,
    poolclass=NullPool, # без этой хуйни будет исключение  RuntimeError: Task <Task ..> got Future attached to a different loop
)

AsyncSessionFactory = async_sessionmaker(
    engine,
    autoflush=False,
    expire_on_commit=False,
)


@pytest_asyncio.fixture(autouse=True, scope="session")
async def init_models(event_loop):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield engine
    async with engine.begin() as conn:

        await conn.run_sync(Base.metadata.drop_all)

@pytest_asyncio.fixture(scope="session")
async def get_db_session() -> AsyncSession:
    async with AsyncSessionFactory() as session:
        yield session
        await session.close()
    # yield AsyncSessionFactory()
