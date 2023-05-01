from sqlalchemy import select
from sqlalchemy.orm import Session
from todobien.db.models import Task


class TaskRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create_task(self, task_dict: dict) -> Task:
        """creates a task or a project if parent_id is None"""
        task = Task(**task_dict)
        try:
            self.session.add(task)
            self.session.commit()

        except Exception:
            self.session.rollback()

        self.session.refresh(task)
        return task

    def update_task(self, *, id: int, task_dict: dict) -> Task | None:
        """updates a task or project"""
        if not (task := self.get_task(id)):
            return None
        try:
            task.update(**task_dict)
            self.session.commit()
        except Exception:
            self.session.rollback()

        self.session.refresh(task)
        return task

    def get_task(self, id: int) -> Task | None:
        return self.session.get(Task, id)

    def get_task_by_name(self, name: str) -> Task | None:
        return self.session.scalars(select(Task).filter_by(name=name)).first()

    def delete_task(self, id: int) -> tuple[Task | None, bool]:
        if not (task := self.get_task(id)):
            return None, False
        try:
            self.session.delete(task)
            self.session.commit()
        except Exception:
            self.session.rollback()

        return task, True

    def get_all_root_tasks(self) -> list[Task] | None:
        return self.session.scalars(select(Task).filter_by(parent_id=None)).all()
