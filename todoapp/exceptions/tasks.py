from dataclasses import dataclass


@dataclass
class ExceptionOfTodoApp(Exception):
    detail: str
    status_code: int


@dataclass
class TaskAlreadyFinished(ExceptionOfTodoApp):
    detail = "Task already finished"
    status_code = 400