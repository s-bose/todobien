from sqlalchemy.engine import Engine, create_engine
from sqlalchemy.orm import sessionmaker

from todobien.config import settings


class DbInstance:
    _engine: Engine = None
    _sessionmaker: sessionmaker = None

    def __init__(self) -> None:
        self._engine = create_engine(f"sqlite:///{settings.SQLITE_DB_PATH}")

        self._sessionmaker = sessionmaker(
            bind=self._engine, autocommit=True, autoflush=True
        )

    @property
    def engine(self):
        return self._engine

    @property
    def session(self):
        return self._sessionmaker()


db_instance = DbInstance()
