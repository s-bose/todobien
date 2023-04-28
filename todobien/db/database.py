from contextlib import contextmanager

from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


@contextmanager
def db_session(db_url):
    engine = create_engine(f"sqlite:///{db_url}")
    connection = engine.connect()
    db_session = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=engine)
    )
    yield db_session
    db_session.close()
    connection.close()
