class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
        else:
            print("Invalid task index.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for task in self.tasks:
            status = "✓" if task.completed else "✗"
            print(f"[{status}] {task.title}: {task.description}")

task_manager = TaskManager()
