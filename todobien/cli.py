import typer
from rich.console import Console

from pathlib import Path

from todobien.models.models import metadata
from todobien.db.database import db_instance
from todobien.models.enums import Priority, Status

metadata.create_all(bind=db_instance.engine)

app = typer.Typer()
console = Console()


@app.command()
def init():
    pth = Path.home() / ".todobien"
    Path.mkdir(pth, exist_ok=True)
    console.print("init")


@app.command()
def add():
    console.print("add")


@app.command()
def edit():
    console.print("edit")


@app.command()
def remove():
    console.print("remove")


@app.command()
def view(
    all: bool = typer.Option(
        False,
        "-a",
        "--all",
        help="show all details for a project / task / subtask",
        is_flag=True,
    ),
    extended: bool = typer.Option(
        False,
        "-e",
        "--ext",
        help="show extended tree for a project / task",
        is_flag=True,
    ),
    compact: bool = typer.Option(
        True,
        "-c",
        "--compact",
        help="show compact view of project / task",
        is_flag=True,
    ),
):
    console.print("view")


@app.command()
def set(
    priority: Priority = typer.Option(
        Priority.LOW,
        autocompletion=lambda: [Priority.LOW, Priority.MEDIUM, Priority.HIGH],
    )
):
    console.print("set")


@app.command()
def stat():
    console.print("stat")
