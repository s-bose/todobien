import os
from pathlib import Path
import typer
import questionary
from rich.console import Console
from rich.prompt import Prompt
from prompt_toolkit.shortcuts import CompleteStyle

from todobien.models.models import Base
from todobien.db.database import db_instance
from todobien.models.enums import Priority, Status
from todobien.config import settings


app = typer.Typer()
console = Console()


@app.command()
def init():
    if Path.exists(settings.SQLITE_DB_PATH):
        console.print("[red bold]database already exists. Skipping init[/red bold]")
        raise typer.Exit()
    else:
        console.print("[green bold]First time setup[/green bold]")
        db_path = questionary.path(
            "Enter db path",
            default=str(settings.SQLITE_DB_PATH),
            complete_style=CompleteStyle.MULTI_COLUMN,
        ).ask()

        if not db_path:
            db_path = str(settings.SQLITE_DB_PATH)

        console.print(
            f"[magenta italic]Setting up db in directory: [green]{db_path}[/green][/magenta italic]"
        )
        console.print("[magenta italic]Creating tables...[/magenta italic]")
        Base.metadata.create_all(bind=db_instance.engine)

        console.print("[green]All set! :confetti_ball: [/green]")


@app.command()
def add(path: str = typer.Option("", help="path to a resource separated by /")):
    if not path:
        console.print("Creating a new project")

    questionary.autocomplete("test", choices=["alpha", "beta"]).ask()


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
