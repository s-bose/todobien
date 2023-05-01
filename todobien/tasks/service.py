from datetime import datetime
import questionary

from sqlalchemy.orm import Session
from todobien.tasks.repository import TaskRepository
from todobien.tasks.exceptions import TaskExists, TaskNotFound
from todobien.cli.forms import new_project_form, new_task_form, update_project_form


class TaskService:
    def __init__(self, session: Session) -> None:
        self.task_repository = TaskRepository(session)

    def create_project(self):
        new_project = new_project_form.ask()

        if self.task_repository.get_task_by_name(new_project["name"]):
            raise TaskExists

        # convert due_date str to datetime
        new_project["due_date"] = datetime.fromisoformat(new_project["due_date"])

        # create project slug
        new_project["slug"] = self.generate_project_slug(new_project["name"])
        return self.task_repository.create_task(new_project)

    def update_project(self):
        all_projects = self.task_repository.get_all_root_tasks()

        name = questionary.select(
            "Choose project:", choices=[p.name for p in all_projects]
        ).ask()
        try:
            selected_project = next(p for p in all_projects if p.name == name)
        except StopIteration:
            raise TaskNotFound

        update_project = update_project_form.ask()

        return self.task_repository.update_task_by_id(
            selected_project.id, update_project
        )

    def create_task(self):
        new_task = new_task_form.ask()

        # convert due_date str to datetime
        new_task["due_date"] = datetime.fromisoformat(new_task["due_date"])

        parent_id = new_task["parent_id"]
        # TODO

    def generate_project_slug(self, project_name: str) -> str:
        try:
            return project_name[:3].upper()
        except IndexError:
            return project_name.upper()
