from dataclasses import dataclass


@dataclass
class ExceptionOfTodoApp(Exception):
    detail: str
    status_code: int
