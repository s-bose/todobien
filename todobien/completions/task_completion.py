from typing import Iterable

from prompt_toolkit.completion import Completer, CompleteEvent, Completion
from prompt_toolkit.document import Document

from todobien.utils import get_path_from_config
from todobien.db.database import db_session
from todobien.services.crud import Crud


class TaskCompleter(Completer):
    min_input_len = 0

    def get_completions(
        self, document: Document, complete_event: CompleteEvent
    ) -> Iterable[Completion]:
        text = document.text_before_cursor

        if len(text) < self.min_input_len:
            return
        # get base name
        text = text.split("/")[-1]

        with db_session(get_path_from_config()) as session:
            crud = Crud(session)
            task = crud.read_by_name(text)
            if not task:
                pass

            subtasks = [subtask for subtask in task.tasks]

            for subtask in subtasks:
                completion = taskname = subtask.name

                if subtask.tasks:
                    taskname += "/"

                yield Completion(text=completion, start_position=0, display=taskname)
