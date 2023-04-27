from databases import Database
from sqlalchemy.engine import Engine, create_engine
from sqlalchemy.orm import sessionmaker

from todobien.config import settings


class DbInstance:
    _engine: Engine = None
    _sessionmaker: sessionmaker = None
    _database: Database = None

    def __init__(self) -> None:
        self._engine = create_engine(settings.SQLITE_DB_STR)

        self._sessionmaker = sessionmaker(
            bind=self._engine, autocommit=True, autoflush=True
        )

        self._database = Database(settings.SQLITE_DB_STR)

    @property
    def engine(self):
        return self._engine

    @property
    def session(self):
        return self._sessionmaker()

    @property
    def database(self):
        return self._database


db_instance = DbInstance()
