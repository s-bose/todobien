from typer import Typer


from pathlib import Path

from todobien.models.models import metadata
from todobien.db.database import db_instance

metadata.create_all(bind=db_instance.engine)

app = Typer()


@app.command()
def init():
    pth = Path.home() / ".todobien"
    Path.mkdir(pth, exist_ok=True)
    print(pth)
