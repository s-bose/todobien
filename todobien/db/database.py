from contextlib import contextmanager

from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from todobien.utils import get_path_from_config


@contextmanager
def db_session():
    db_url = get_path_from_config()
    engine = create_engine(f"sqlite:///{db_url}")
    connection = engine.connect()
    db_session = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=engine)
    )
    yield db_session
    db_session.close()
    connection.close()
