from os import walk
import typer
from rich.console import Console

from pathlib import Path

from todobien.models.models import Base
from todobien.db.database import db_instance
from todobien.models.enums import Priority, Status

Base.metadata.create_all(bind=db_instance.engine)

app = typer.Typer()
console = Console()


@app.command()
def init():
    pth = Path.home() / ".todobien"
    Path.mkdir(pth, exist_ok=True)

    console.print("init")


@app.command()
def add(path: str = typer.Option("", help="path to a resource separated by /")):
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
    path: str = typer.Option("", rich_help_panel="path to a resource separated by /"),
):
    console.print("view")


@app.command()
def set(
    priority: Priority = typer.Option(Priority.LOW, "-x", "-X", "--priority"),
    status: Status = typer.Option(Status.TODO, "-s", "-S", "--status"),
    estimate: str = typer.Option("", "-E", "--estimate"),
    due: str = typer.Option(
        "",
        "-D",
        "--due",
        rich_help_panel="Due date for completion: Format: [green]yyyy-mm-dd[/green]",
    ),
    path: str = typer.Option("", rich_help_panel="path to a resource separated by /"),
):
    console.print("set")


@app.command()
def stat():
    console.print("stat")
