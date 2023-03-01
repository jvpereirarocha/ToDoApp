from enum import Enum


class StatusOfTask(Enum):
    NEW = "new"
    TODO = "todo"
    DOING = "doing"
    DONE = "done"
    DELETED = "deleted"
    CLOSED = "closed"
