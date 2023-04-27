from pathlib import Path
from pydantic import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    SQLITE_DB_PATH: Path = Path.home() / ".todobien" / "main.sqlite"
    SQLITE_DB_STR: str = f"sqlite:///{str(SQLITE_DB_PATH)}"
    TODOBIEN_CONFIG_DIR = Path.home() / ".todobien"


settings = Settings()
