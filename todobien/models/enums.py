import enum


class TaskType(str, enum.Enum):
    FEATURE = "FEATURE"
    BUG = "BUG"


class Status(str, enum.Enum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    PAUSED = "PAUSED"
    BACKLOG = "BACKLOG"
    DONE = "DONE"
    CANCELED = "CANCELED"


class Priority(str, enum.Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
