import json
from Task import Task
from TaskNotFoundError import TaskNotFoundError

class TaskManager:
    def __init__(self):
        self.tasks = []
        self._id_count = 0
    def task_add(self, desc):
        new_task = Task(self._id_count, desc, "todo")
        self.tasks.append(new_task)
        self._id_count += 1
        return new_task

    def task_update(self, id, desc):
        task = self._find_task(id)
        if task:
            task.task_update(desc)

    def task_delete(self, id):
        task = self._find_task(id)
        if task:
            self.tasks.remove(task)

    def task_mark_in_progress(self, id):
        task = self._find_task(id)
        if task:
            task.task_mark_in_progress()   

    def task_mark_done(self, id):
        task = self._find_task(id)
        if task:
            task.task_mark_done()   

    def task_list(self, status=None):
        if status == None:
            return self.tasks
        return [t for t in self.tasks if t.status == status]

    def _find_task(self, id):
        for t in self.tasks:
            if t.id == id:
                return t
        raise TaskNotFoundError(f"Task with ID {id} does not exist.")
    
    def save_to_file(self, filename="tasks.json"):
        with open(filename, 'w') as f:
            json.dump([t.to_dict() for t in self.tasks], f, indent=2)

    def load_from_file(self, filename="tasks.json"):
        from pathlib import Path
        file_path = Path(filename)
        
        if not file_path.exists() or file_path.stat().st_size == 0:
            # File does not exist or is empty, start fresh
            self.tasks = []
            self._id_count = 0
            return

        try:
            with file_path.open('r') as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(d) for d in data]
                if self.tasks:
                    self._id_count = max(t.id for t in self.tasks) + 1

        except json.JSONDecodeError:
            # Corrupted file, reset
            print(f"Warning: {filename} is corrupted. Starting fresh.")
            self.tasks = []
            self._id_count = 0
