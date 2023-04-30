from datetime import date
from todobien.db.database import db_session
from todobien.models.models import Task
from todobien.services.crud import Crud
from todobien.utils import get_path_from_config


def check_date(date_str: str) -> bool:
    try:
        date.fromisoformat(date_str)
        return True
    except ValueError:
        return False


def validate_path(path: str):
    """validates if a resource path is correct"""
    resources = path.split("/")
    db_path = get_path_from_config()

    with db_session(db_path) as session:
        crud = Crud(session)

        parent = None
        name = None
        for resource in resources:
            task = crud.read_by_name(resource)
            if task is None:
                raise ValueError(f"Task: {resource} not found")

            if task.parent_id == parent:
                parent = task.id
                name = task.name
            else:
                raise ValueError(f"Task: {resource} not found under {name}")
