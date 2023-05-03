import questionary
from datetime import datetime

form = questionary.form(
    name=questionary.text("name?", default=""),
    age=questionary.text("age?", default="12"),
    dob=questionary.text("dob?", default="2023-08-31"),
)

answer = form.ask()
try:
    datetime.fromisoformat(answer["dob"])
except (ValueError, TypeError):
    print("Invalid date")

print(answer)
