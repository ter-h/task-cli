from task_cli.TaskManager import TaskManager
from task_cli.TaskNotFoundError import TaskNotFoundError

def test_add_task():
    tm = TaskManager()

    task = tm.task_add("Buy Milk")

    assert task.id == 1
    assert task.description == "Buy Milk"
    assert task.status == "todo"