from dataclasses import dataclass

from todoapp.exceptions.base import ExceptionOfTodoApp


@dataclass
class TaskAlreadyFinished(ExceptionOfTodoApp):
    detail = "Task already finished"
    status_code = 400
