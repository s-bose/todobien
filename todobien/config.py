from pathlib import Path
from pydantic import BaseSettings


class Settings(BaseSettings):
    SQLITE_DB_PATH: Path = Path.home() / ".todobien" / "main.db"
    SQLITE_DB_STR: str = f"sqlite:///{str(SQLITE_DB_PATH)}"


settings = Settings()
