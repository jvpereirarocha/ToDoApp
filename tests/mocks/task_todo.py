from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4
from pytest import fixture
from todoapp.entities.tasks import TasksToDo
from todoapp.object_values.status_of_tasks import StatusOfTask


@fixture(scope="function")
def mock_task_todo():
    def _make_new_mock(
        description: str,
        status: StatusOfTask,
        created_at: datetime,
        finished: bool,
        finished_at: Optional[datetime] = None,
    ):
        new_task = TasksToDo(
            task_id=uuid4().hex,
            description=description,
            status=status,
            created_at=created_at,
            finished=finished,
            finished_at=finished_at,
        )

        return new_task

    return _make_new_mock
