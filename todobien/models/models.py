from datetime import datetime
from sqlalchemy import String, Integer, JSON, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, declarative_base, mapped_column

Base = declarative_base()


class Task(Base):
    __tablename__ = "task"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    description: Mapped[str] = mapped_column(String, nullable=True)
    links: Mapped[str] = mapped_column(String, nullable=True)
    additional_data: Mapped[dict] = mapped_column(JSON, nullable=True)
    is_done: Mapped[bool] = mapped_column(Boolean, default=False)
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)
    parent_id: Mapped[int] = mapped_column(Integer, ForeignKey("task.id"))

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    due_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
