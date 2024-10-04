from dateutil.parser import parse
from datetime import date, timedelta, datetime
import questionary
from dataclasses import fields, dataclass

from todobien.utils import generate_project_slug
from todobien.cli.validators import check_date, validate_estimate, validate_slug
from todobien.constants import Priority, Status


class QuestionaryMixin:
    """a mixin class for dataclasses to automatically
    create a questionary form from the dataclass fields"""

    @classmethod
    def create_form(cls, **kwargs):
        form_data = {}
        for field in fields(cls):
            if isinstance(field.default, questionary.Question):
                form_data[field.name] = field.default
        answer_dict = questionary.form(**form_data).ask()

        for field in fields(cls):
            if not isinstance(field.default, questionary.Question):
                continue
            if answer_dict[field.name] is None:
                raise ValueError
            if field.type == int:
                value = int(answer_dict[field.name])
            elif field.type == float:
                value = float(answer_dict[field.name])
            elif field.type == datetime:
                value = parse(answer_dict[field.name])
            else:
                value = answer_dict[field.name]

            answer_dict[field.name] = value
        return cls(**answer_dict, **kwargs)


@dataclass
class NewProject(QuestionaryMixin):
    name: str = questionary.text("Name of the project:", validate=lambda x: len(x) > 0)
    slug: str = questionary.text(
        "Project slug:",
        default=generate_project_slug(),  # TODO - howto get `name` input after asking
        validate=validate_slug,
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


@dataclass
class UpdateProject(QuestionaryMixin):
    description: str = questionary.text("Description:", default="")
    links: str = questionary.text("Links:", default="")
    priority: Priority = questionary.select(
        "Priority:", choices=Priority.list_values(), default=None
    )
    status: Status = questionary.select(
        "Status:", choices=Status.list_values(), default=None
    )
    estimate: str = questionary.text(
        "Estimate:",
        instruction="estimate delta [mo-w-d-h-m]",
        default="7d",
        validate=validate_estimate,
    )


@dataclass
class NewTask(QuestionaryMixin):
    parent_id: int
    name: str = (questionary.text("Name of the task:", validate=lambda x: len(x) > 0),)
    description: str = (questionary.text("Description:", default=""),)
    links: str = (questionary.text("Links:", default=""),)
    priority: Priority = (
        questionary.select(
            "Priority:", choices=Priority.list_values(), default=Priority.LOW
        ),
    )
    due_date: datetime = (
        questionary.text(
            "Due date:",
            instruction="[yyyy-mm-dd]",
            default=str(date.today() + timedelta(days=7)),
            validate=check_date,
        ),
    )
    estimate: str = (
        questionary.text(
            "Estimate:",
            instruction="estimate delta [mo-w-d-h-m]",
            default="7d",
            validate=validate_estimate,
        ),
    )


@dataclass
class UpdateTask(QuestionaryMixin):
    parent_id: int
    description: str = questionary.text("Description:", default="")
    links: str = questionary.text("Links:", default="")
    priority: Priority = questionary.select(
        "Priority:", choices=Priority.list_values(), default=None
    )
    status: Status = questionary.select(
        "Status:", choices=Status.list_values(), default=None
    )
    estimate: str = questionary.text(
        "Estimate:",
        instruction="estimate delta [mo-w-d-h-m]",
        default="7d",
        validate=validate_estimate,
    )
