# task_manager.py

from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class Task:
    title: str
    priority: int
    completed: bool = False
    created_at: datetime = datetime.now()

    def complete(self):
        self.completed = True


class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, title: str, priority: int):
        self.tasks.append(Task(title, priority))

    def complete_task(self, title: str):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                task.complete()
                return True
        return False

    def pending_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def print_summary(self):
        print("\n=== Task Summary ===")
        for task in sorted(self.tasks, key=lambda t: t.priority):
            status = "✓" if task.completed else "•"
            print(
                f"{status} "
                f"[Priority {task.priority}] "
                f"{task.title} "
                f"({task.created_at.strftime('%Y-%m-%d %H:%M')})"
            )


def main():
    manager = TaskManager()

    manager.add_task("Write documentation", 2)
    manager.add_task("Fix login bug", 1)
    manager.add_task("Review pull request", 3)
    manager.add_task("Deploy to staging", 2)

    manager.complete_task("Fix login bug")

    manager.print_summary()

    print("\nPending Tasks:")
    for task in manager.pending_tasks():
        print(f"- {task.title}")


if __name__ == "__main__":
    main()
