class Task:
    def __init__(self, title, description, completed=False):
        self.title = title
        self.description = description
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title}: {self.description}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        new_task = Task(title, description)
        self.tasks.append(new_task)
        print(f"Added task: {title}")

    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_completed()
                print(f"Completed task: {title}")
                return
        print(f"Task not found: {title}")

    def show_tasks(self):
        for task in self.tasks:
            print(task)


if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Write code", "Write code for the new feature")
    manager.add_task("Review PR", "Review the pull request from the team")
    manager.show_tasks()
    manager.complete_task("Write code")
    manager.show_tasks()
