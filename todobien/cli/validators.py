from datetime import date
from todobien.db.database import db_session

from todobien.constants import ESTIMATE_KEYS
from todobien.tasks.repository import TaskRepository


def check_date(date_str: str) -> bool:
    try:
        date.fromisoformat(date_str)
        return True
    except ValueError:
        return False


def validate_path(path: str):
    """validates if a resource path is correct"""
    resources = path.split("/")

    with db_session() as session:
        task_repo = TaskRepository(session)

        parent = None
        name = None
        for resource in resources:
            task = task_repo.get_task_by_name(resource)
            if task is None:
                raise ValueError(f"Task: {resource} not found")

            if task.parent_id == parent:
                parent = task.id
                name = task.name
            else:
                raise ValueError(f"Task: {resource} not found under {name}")


def validate_task(task_str: str) -> bool:
    if len(task_str) == 0:
        return False

    with db_session() as session:
        return False if TaskRepository(session).get_task_by_name(task_str) else True


def validate_estimate(estimare_str: str) -> bool:
    segments = estimare_str.split(" ")
    for segment in segments:
        if segment.endswith(ESTIMATE_KEYS) and segment[0].isdigit():
            continue
        else:
            return False

    return True


def validate_slug(slug: str) -> bool | None:
    with db_session() as session:
        tasks_with_slug = TaskRepository(session).get_task_by_slug(slug)
        if tasks_with_slug or len(tasks_with_slug) > 0:
            raise ValueError("slug already exists")

        return True
