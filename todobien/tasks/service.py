from datetime import datetime

from sqlalchemy.orm import Session
from todobien.tasks.repository import TaskRepository
from todobien.cli.forms import new_project_form, new_task_form


class TaskService:
    def __init__(self, session: Session) -> None:
        self.task_repository = TaskRepository(session)

    def create_project(self):
        new_project = new_project_form.ask()

        # convert due_date str to datetime
        new_project["due_date"] = datetime.fromisoformat(new_project["due_date"])

        return self.task_repository.create_task(new_project)

    def create_task(self):
        new_task = new_task_form.ask()

        # convert due_date str to datetime
        new_task["due_date"] = datetime.fromisoformat(new_task["due_date"])

        parent_id = new_task["parent_id"]
        return
