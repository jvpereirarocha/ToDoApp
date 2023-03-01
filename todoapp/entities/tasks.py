from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import uuid4, UUID
from todoapp.exceptions.tasks import TaskAlreadyFinished
from todoapp.object_values.status_of_tasks import StatusOfTask


@dataclass
class TasksToDo:
    task_id: UUID
    description: str
    status: StatusOfTask
    created_at: datetime
    finished: bool = False
    finished_at: Optional[datetime] = None

    @classmethod
    def new_task(cls, description: str):
        return cls(
            task_id=uuid4().hex,
            description=description,
            created_at=datetime.now(),
            status=StatusOfTask.NEW,
            finished=False
        )
    
    
    def update_task_status(self, status: StatusOfTask):
        self.status = status

    def finish_task(self):
        if self.finished:
            raise TaskAlreadyFinished(detail="Task already finished", status_code=400)
        self.finished = True
        self.status = StatusOfTask.DONE
        self.finished_at = datetime.now()
