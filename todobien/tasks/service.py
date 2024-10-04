from dataclasses import asdict
import questionary

from sqlalchemy.orm import Session
from prompt_toolkit.completion import NestedCompleter
from prompt_toolkit.shortcuts import CompleteStyle

from todobien.tasks.repository import TaskRepository
from todobien.tasks.exceptions import TaskExists, TaskNotFound
from todobien.cli.forms import NewProject
from todobien.db.models import Task
from todobien.db.database import db_session


class TaskService:
    def __init__(self, session: Session) -> None:
        self.task_repository = TaskRepository(session)

    def create_project(self):
        new_project: NewProject = NewProject.create_form()

        if self.task_repository.get_task_by_name(new_project.name):
            raise TaskExists

        return self.task_repository.create_task(asdict(new_project))

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

    def construct_task_tree(self):
        def _recurse_tree(node: Task):
            if node.tasks and len(node.tasks) != 0:
                return {task.slug: _recurse_tree(task) for task in node.tasks}
            else:
                return None

        root = self.task_repository.get_all_root_tasks()
        root_tree = {node.name: _recurse_tree(node) for node in root}
        return root_tree

    def create_task(self):
        task_dict = self.construct_task_tree()
        meta = {
            "unsaver": "a web app to browse and declutter your reddit saved posts",
            "todobien": "a cli-based task management app",
            "1": "add additional fields",
        }

        completer = NestedCompleter.from_nested_dict(task_dict)
        # text = prompt("enter task path:", completer=completer)
        text = questionary.autocomplete(
            "enter task path:",
            choices=task_dict,
            completer=completer,
            complete_style=CompleteStyle.MULTI_COLUMN,
        ).ask()
        print(text)
        # new_task = new_task_form.ask()

        # # convert due_date str to datetime
        # new_task["due_date"] = datetime.fromisoformat(new_task["due_date"])
        # new_task["parent_id"] = parent.id
        # new_task["slug"] = len(parent.tasks) + 1
        # return self.task_repository.create_task(new_task)


if __name__ == "__main__":
    with db_session() as session:
        d = TaskService(session).construct_task_tree()
        print(d)
