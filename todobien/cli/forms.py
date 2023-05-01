from datetime import date, timedelta
import questionary

from todobien.cli.validators import check_date, validate_estimate
from todobien.constants import Priority, Status

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
