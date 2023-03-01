from pytest import raises
from datetime import datetime
from todoapp.entities.tasks import TasksToDo
from todoapp.exceptions.tasks import TaskAlreadyFinished
from todoapp.object_values.status_of_tasks import StatusOfTask


def test_create_new_task():
    description_of_task = "Learn English"
    task = TasksToDo.new_task(
        description=description_of_task
    )

    assert task.status == StatusOfTask.NEW
    assert task.finished is False


def test_update_task_status(mock_task_todo):
    task: TasksToDo = mock_task_todo(
        description="Learn English",
        status=StatusOfTask.NEW,
        created_at=datetime.now(),
        finished=False,
    )
    assert task.finished is False
    assert task.finished_at is None
    
    task.update_task_status(status=StatusOfTask.TODO)
    assert task.finished is False
    assert task.status == StatusOfTask.TODO
    assert task.finished_at is None

    task.update_task_status(status=StatusOfTask.DOING)
    assert task.finished is False
    assert task.status == StatusOfTask.DOING
    assert task.finished_at is None

    task.finish_task()
    assert task.finished is True
    assert task.status == StatusOfTask.DONE
    assert task.finished_at is not None


def test_raise_exception_when_task_is_already_finished(mock_task_todo):
    task: TasksToDo = mock_task_todo(
        description="Play videogame",
        status=StatusOfTask.DONE,
        created_at=datetime.now(),
        finished=True,
    )

    with raises(TaskAlreadyFinished) as exc:
        task.finish_task()
        exc.detail == "Task already finished"
        exc.status_code == 400
