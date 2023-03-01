from dataclasses import dataclass

from todoapp.exceptions.base import ExceptionOfTodoApp


@dataclass
class InvalidStatusOfTask(ExceptionOfTodoApp):
    detail = "This status is not valid"
    status_code = 400
