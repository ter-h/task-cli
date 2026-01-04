from datetime import datetime
class Task:
    def __init__(self, id, description, status, createdAt=None, updatedAt=None):
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = createdAt or datetime.now()
        self.updatedAt = updatedAt or datetime.now()

    def task_update(self, new_desc):
        self. description = new_desc
        self.updatedAt = datetime.now()
    
    def mark_todo(self):
        self.status = "todo"
        self.updatedAt = datetime.now()

    def mark_in_progress(self):
        self.status = "in-progress"
        self.updatedAt = datetime.now()

    def mark_done(self):
        self.status = "done"
        self.updatedAt = datetime.now()

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": str(self.status),
            "createdAt": self.createdAt.isoformat(),
            "updatedAt": self.updatedAt.isoformat()
        }
    
    @staticmethod
    def from_dict(data):
        return Task(
            id=data["id"],
            description=data["description"],
            status=data["status"].lower(),
            createdAt=datetime.fromisoformat(data["createdAt"]),
            updatedAt=datetime.fromisoformat(data["updatedAt"])
        )