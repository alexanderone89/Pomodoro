from typing import Any, Optional

from sqlalchemy.orm import (DeclarativeMeta,
                            Mapped,
                            declarative_base,
                            mapped_column, DeclarativeBase, declared_attr)


class Base(DeclarativeBase):
    id: Any
    __name__: str
    __allow_unmapped = True

    @declared_attr
    def __tablename__(self)->str:
        return self.__name__.lower()

# Base = declarative_base()

class Tasks(Base):
    __tablename__ = 'Tasks'

    id : Mapped[int] = mapped_column(primary_key=True )
    name : Mapped[str]
    pomodoro_count : Mapped[int]
    category_id : Mapped[int]

class Categories(Base):
    __tablename__ = 'Categories'

    id : Mapped[str] = mapped_column(primary_key=True )
    name : Mapped[str]
    type : Mapped[Optional[str]]
