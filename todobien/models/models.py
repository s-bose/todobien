from typing import ForwardRef
from datetime import datetime
import ormar as om
from ormar import Model
from sqlalchemy import MetaData

from todobien.db.database import db_instance

metadata = MetaData()

TaskRef = ForwardRef("Task")


class Task(Model):
    class Meta:
        metadata = metadata
        database = db_instance.database

    id: int = om.Integer(primary_key=True, autoincrement=True)
    name: str = om.String(max_length=100, unique=True)
    description: str = om.Text(nullable=True)
    links: str = om.Text(nullable=True)
    additional_data: dict = om.JSON(nullable=True)
    is_done: bool = om.Boolean(default=False)
    is_deleted: bool = om.Boolean(default=False)

    parent: TaskRef = om.ForeignKey(TaskRef, nullable=True)

    created_at: datetime = om.DateTime(default=datetime.now())
    updated_at: datetime = om.DateTime(default=datetime.now())
    due_date: datetime = om.DateTime(nullable=False)


Task.update_forward_refs()
