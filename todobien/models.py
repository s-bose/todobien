from typing import Optional, List
from uuid import UUID
from datetime import datetime

from pydantic import BaseModel


class Project(BaseModel):
    id: UUID
    name: str
    author: str
    tag: Optional[str]
    description: Optional[str]
    tasks: List["Task"]
    created_at: datetime
    updated_at: datetime
    priority: str
    due_date: datetime
    is_done: bool
    is_deleted: bool


class Task(BaseModel):
    slug: str
    tag: str
    project_id: UUID
    created_at: datetime
    updated_at: datetime
    priority: str
    due_date: datetime
    is_done: bool
    is_deleted: bool
