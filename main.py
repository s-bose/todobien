from rich.console import Console
from rich.table import Table
import datetime

import time
from rich.progress import track

table = Table(title="Projects")
table.add_column("project", justify="right", style="cyan", no_wrap=True)
table.add_column("status", justify="center", style="magenta", no_wrap=True)
table.add_column("priority", justify="center", no_wrap=True)
table.add_column("due", justify="right", no_wrap=True)


table.add_row(
    "unsaver", "IN_PROGRESS", "[red]HIGH[/red]", str(datetime.date(2023, 5, 10))
)
table.add_row(
    "todobien", "IN_PROGRESS", "[green]MEDIUM[/green]", str(datetime.date(2023, 5, 20))
)


console = Console()
console.print(table)

from time import sleep

from rich.table import Column
from rich.progress import Progress, BarColumn, TextColumn

text_column = TextColumn("{task.description}", table_column=Column(ratio=1))
bar_column = BarColumn(bar_width=None, table_column=Column(ratio=2))
progress = Progress(text_column, bar_column, expand=True)

with progress:
    for n in progress.track(range(100)):
        progress.print(n)
        sleep(0.1)
