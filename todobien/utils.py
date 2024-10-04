from typing import Optional
from configparser import ConfigParser
from todobien.config import settings


def get_path_from_config() -> str | None:
    config = ConfigParser()
    config.read(settings.CONFIG_PATH)
    try:
        return config["database"]["path"]
    except KeyError:
        return None


def generate_project_slug(project_name: str) -> str:
    try:
        return project_name[:3].upper()
    except IndexError:
        return project_name.upper()


def create_config(database: Optional[str] = None) -> None:
    config = ConfigParser()
    config["database"] = {"path": database or str(settings.SQLITE_DB_PATH)}

    with open(settings.CONFIG_PATH, "w") as file:
        config.write(file)
