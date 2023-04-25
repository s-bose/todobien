from typing import Self
import enum


class BaseEnum(str, enum.Enum):
    def __str__(self) -> str:
        return self.value

    def __eq__(self, other: str | Self) -> bool:
        if isinstance(other, str):
            return self.value.casefold() == other.casefold()
        return super().__eq__(other)


class Status(BaseEnum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    PAUSED = "PAUSED"
    BACKLOG = "BACKLOG"
    DONE = "DONE"
    CANCELED = "CANCELED"


class Priority(BaseEnum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
