class TaskExists(Exception):
    """task with name already exists"""


class TaskNotFound(Exception):
    """task not found"""


class InvalidParent(Exception):
    """specified parent task is invalid"""
