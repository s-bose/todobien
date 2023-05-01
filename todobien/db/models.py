from datetime import datetime
from sqlalchemy import String, Integer, JSON, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship

from todobien.constants import Priority, Status

Base = declarative_base()


class Task(Base):
    __tablename__ = "task"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    description: Mapped[str] = mapped_column(String, nullable=True)
    links: Mapped[str] = mapped_column(String, nullable=True)
    additional_data: Mapped[dict] = mapped_column(JSON, nullable=True)
    slug: Mapped[str] = mapped_column(String, nullable=False)
    is_done: Mapped[bool] = mapped_column(Boolean, default=False)
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)
    parent_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("task.id"), nullable=True
    )
    priority: Mapped[str] = mapped_column(String, default=Priority.LOW)
    status: Mapped[str] = mapped_column(String, default=Status.TODO)
    estimate: Mapped[str] = mapped_column(String, nullable=True, default="7d")

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(), onupdate=datetime.now()
    )
    due_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    tasks = relationship("Task")
