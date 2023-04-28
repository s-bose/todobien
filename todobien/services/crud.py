from typing import Dict
from sqlalchemy import select

from todobien.models.models import Task
from todobien.db.database import db_instance


class Crud:
    def __init__(self) -> None:
        self.model = Task
        self.session = db_instance.session

    def create(self, task_dict: Dict) -> Task | None:
        task = Task(**task_dict)
        self.session.add(task)
        self.session.commit()
        return task

    def read(self, id: int) -> Task | None:
        stmt = select(self.model).where(self.model.id == id)

        return self.session.scalars(stmt).one()

    async def read_by_name(self, name: str) -> Task | None:
        stmt = select(self.model).where(self.model.name == name)

        return self.session.scalars(stmt).one()
