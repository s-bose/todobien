from typing import Iterable, Optional

from prompt_toolkit.completion import (
    Completer,
    CompleteEvent,
    Completion,
    PathCompleter,
)
from prompt_toolkit.document import Document
from todobien.db.database import db_session
from todobien.tasks.repository import TaskRepository
from todobien.db.models import Task


class TaskCompleter(Completer):
    min_input_len = 1

    def __init__(self, session) -> None:
        super().__init__()
        self.session = session
        self.task_repository = TaskRepository(session)

    def get_project_dirs(self, name: Optional[str] = None) -> list[Task]:
        if name:
            task = self.task_repository.get_task_by_name(name)
            return task.tasks if task else None
        else:
            return self.task_repository.get_all_root_tasks() or None

    def get_completions(
        self, document: Document, complete_event: CompleteEvent
    ) -> Iterable[Completion]:
        text = document.text_before_cursor

        if len(text) < self.min_input_len:
            return

        # get base name
        print(f"{text=}")
        if not text:
            task_directories = self.get_project_dirs()
        else:
            task_directories = self.get_project_dirs(text)

        for task in task_directories:
            completion = taskname = task.name

            if task.tasks:
                completion += "/"

            yield Completion(text=completion, start_position=0, display=taskname)
