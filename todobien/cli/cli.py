from datetime import date, timedelta, datetime
from pathlib import Path
from todobien.cli.validators import check_date
import typer
import questionary
from rich.console import Console
from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter
from prompt_toolkit.shortcuts import CompleteStyle
from sqlalchemy.engine import create_engine

from todobien.db.models import Base
from todobien.constants import Priority, Status
from todobien.config import settings
from todobien.utils import get_path_from_config, create_config

from todobien.db.database import db_session
from todobien.tasks.service import TaskService
from todobien.tasks.exceptions import TaskExists
from todobien.completions.task_completion import TaskCompleter

app = typer.Typer()
console = Console()


@app.command()
def init():
    if get_path_from_config():
        console.print("[red bold]database already exists. Skipping init[/red bold]")
        raise typer.Exit()
    else:
        console.print("[green bold]First time setup[/green bold]")
        db_path = questionary.path(
            "Enter db path",
            default=str(settings.SQLITE_DB_PATH),
            complete_style=CompleteStyle.MULTI_COLUMN,
        ).ask()

        db_path = Path(db_path).resolve()
        console.print(
            f"[magenta italic]Setting up db in directory: [green]{db_path}[/green][/magenta italic]"
        )
        create_config(database=db_path)

        engine = create_engine(f"sqlite:///{db_path}")
        Base.metadata.create_all(bind=engine)
        console.print("[magenta italic]Creating tables...[/magenta italic]")
        console.print("[green]All set! :confetti_ball: [/green]")


@app.command()
def add(
    path: str = typer.Option(
        "", "-p", "--path", help="path to a resource separated by /"
    )
):
    if not get_path_from_config():
        console.print(
            "todobien is not initialized yet! Run [italic]todobien init[/italic] first!",
            style="red bold",
        )
        raise typer.Exit()

    # TODO - handle `--path` later
    choice = questionary.select("Creating new", choices=["project", "task"]).ask()
    match choice:
        case "project":
            with db_session() as session:
                try:
                    new_project = TaskService(session).create_project()
                    console.print(
                        f"created new project {new_project.name} ({new_project.slug})"
                    )
                except TaskExists:
                    typer.echo("Project already exists! Skipping.")
                    raise typer.Abort()
        case "task":
            with db_session() as session:
                try:
                    task_svc = TaskService(session)
                    task_svc.create_task()
                except TaskExists:
                    typer.echo("Task already exists! Skipping.")
                    raise typer.Abort()


@app.command()
def edit(
    path: str = typer.Option(
        "", "-p", "--path", help="path to a resource separated by /"
    )
):
    if not path:
        choice = questionary.select("Edit", choices=["project", "task"]).ask()
        match choice:
            case "project":
                with db_session() as session:
                    TaskService(session).update_project()
            case "task":
                raise typer.Abort()


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


@app.command()
def purge():
    answer = questionary.confirm("Remove db. Are you sure?", default=False).ask()
    if answer:
        db_path = get_path_from_config()
        Path(db_path).unlink(missing_ok=True)
        settings.CONFIG_PATH.unlink(missing_ok=True)
        console.print("[green]Database successfully removed[/green]")
