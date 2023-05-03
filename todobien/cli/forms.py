from datetime import date, timedelta, datetime
import questionary
from dataclasses import fields, dataclass

from todobien.cli.validators import check_date, validate_estimate
from todobien.constants import Priority, Status


class QuestionaryMixin:
    """a mixin class for dataclasses to automatically
    create a questionary form from the dataclass fields"""

    @classmethod
    def create_form(cls):
        form_data = {}
        for field in fields(cls):
            form_data[field.name] = field.default
        answer_dict = questionary.form(**form_data).ask()

        for field in fields(cls):
            if answer_dict[field.name] is None:
                raise ValueError

            if field.type == int:
                value = int(answer_dict[field.name])
            elif field.type == float:
                value = float(answer_dict[field.name])
            elif field.type == datetime:
                value = datetime.fromisoformat(answer_dict[field.name])
            else:
                value = answer_dict[field.name]

            answer_dict[field.name] = value
        return cls(**answer_dict)


new_project_form = questionary.form(
    name=questionary.text("Name of the project:", validate=lambda x: len(x) > 0),
    description=questionary.text("Description:", default=""),
    links=questionary.text("Links:", default=""),
    priority=questionary.select(
        "Priority:", choices=Priority.list_values(), default=Priority.LOW
    ),
    due_date=questionary.text(
        "Due date:",
        instruction="[yyyy-mm-dd]",
        default=str(date.today() + timedelta(days=7)),
        validate=check_date,
    ),
)

update_project_form = questionary.form(
    description=questionary.text("Description:", default=""),
    links=questionary.text("Links:", default=""),
    priority=questionary.select(
        "Priority:", choices=Priority.list_values(), default=None
    ),
    status=questionary.select("Status:", choices=Status.list_values(), default=None),
    estimate=questionary.text("Estimate:"),
)

new_task_form = questionary.form(
    name=questionary.text("Name of the task:", validate=lambda x: len(x) > 0),
    description=questionary.text("Description:", default=""),
    links=questionary.text("Links:", default=""),
    priority=questionary.select(
        "Priority:", choices=Priority.list_values(), default=Priority.LOW
    ),
    due_date=questionary.text(
        "Due date:",
        instruction="[yyyy-mm-dd]",
        default=str(date.today() + timedelta(days=7)),
        validate=check_date,
    ),
    estimate=questionary.text(
        "Estimate:",
        instruction="estimate delta [mo-w-d-h-m]",
        default="7d",
        validate=validate_estimate,
    ),
)

if __name__ == "__main__":

    @dataclass
    class NewProjectForm(QuestionaryMixin):
        name: str = questionary.text(
            "Name of the project:", validate=lambda x: len(x) > 0
        )
        description: str = questionary.text("Description:", default="")
        links: str = questionary.text("Links:", default="")
        priority: Priority = questionary.select(
            "Priority:", choices=Priority.list_values(), default=Priority.LOW
        )

        due_date: datetime = questionary.text(
            "Due date:",
            instruction="[yyyy-mm-dd]",
            default=str(date.today() + timedelta(days=7)),
            validate=check_date,
        )

    result = NewProjectForm.create_form()
    print(result)
