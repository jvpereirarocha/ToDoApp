from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
from uuid import uuid4, UUID
from todoapp.exceptions.status_of_task import InvalidStatusOfTask
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
    deleted: bool = False

    @property
    def valid_status(self) -> List[StatusOfTask]:
        return [
            StatusOfTask.NEW,
            StatusOfTask.TODO,
            StatusOfTask.DOING,
            StatusOfTask.DONE,
            StatusOfTask.CLOSED,
            StatusOfTask.DELETED,
        ]

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
        if status not in self.valid_status:
            raise InvalidStatusOfTask(
                detail="This status is not valid",
                status_code=400
            )
        
        self.status = status

    def finish_task(self):
        if self.finished:
            raise TaskAlreadyFinished(detail="Task already finished", status_code=400)
        self.finished = True
        self.status = StatusOfTask.DONE
        self.finished_at = datetime.now()

    def delete_task(self):
        self.deleted = True
