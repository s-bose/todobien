from pathlib import Path
from pydantic import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    TODOBIEN_CONFIG_DIR = Path.home() / ".todobien"
    SQLITE_DB_PATH: Path = TODOBIEN_CONFIG_DIR / "main.db"
    CONFIG_PATH = TODOBIEN_CONFIG_DIR / ".todobien.ini"


settings = Settings()
