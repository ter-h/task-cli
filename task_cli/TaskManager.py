import json
from pathlib import Path
from task_cli.Task import Task
from task_cli.TaskNotFoundError import TaskNotFoundError

class TaskManager:
    def __init__(self):
        # Store tasks in user environment folder
        self.app_dir = Path.home() / ".task-cli"
        self.app_dir.mkdir(exist_ok=True)  # create folder if missing
        self.data_file = self.app_dir / "tasks.json"

        self.tasks = []
        self._id_count = 0
        self.load_from_file()

    def task_add(self, desc):
        new_task = Task(self._id_count, desc, "todo")
        self.tasks.append(new_task)
        self._id_count += 1
        self.save_to_file()
        return new_task

    def task_update(self, id, desc):
        task = self._find_task(id)
        task.task_update(desc)
        self.save_to_file()

    def task_delete(self, id):
        task = self._find_task(id)
        self.tasks.remove(task)
        self.save_to_file()

    def task_mark_in_progress(self, id):
        task = self._find_task(id)
        task.mark_in_progress()
        self.save_to_file()

    def task_mark_todo(self, id):
        task = self._find_task(id)
        task.mark_todo()
        self.save_to_file()
    

    def task_mark_done(self, id):
        task = self._find_task(id)
        task.mark_done()
        self.save_to_file()

    def task_list(self, status=None):
        if status is None:
            return self.tasks
        return [t for t in self.tasks if t.status == status]

    def _find_task(self, id):
        for t in self.tasks:
            if t.id == id:
                return t
        raise TaskNotFoundError(f"Task with ID {id} does not exist.")

    def save_to_file(self):
        with self.data_file.open('w') as f:
            json.dump([t.to_dict() for t in self.tasks], f, indent=2)

    def load_from_file(self):
        if not self.data_file.exists() or self.data_file.stat().st_size == 0:
            # File missing or empty, start fresh
            self.tasks = []
            self._id_count = 0
            return

        try:
            with self.data_file.open('r') as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(d) for d in data]
                if self.tasks:
                    self._id_count = max(t.id for t in self.tasks) + 1
        except json.JSONDecodeError:
            print(f"Warning: {self.data_file} is corrupted. Starting fresh.")
            self.tasks = []
            self._id_count = 0
