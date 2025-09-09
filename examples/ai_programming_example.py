"""
AI Programming Examples
This file demonstrates various AI-assisted programming patterns and techniques.
"""

import requests
import json
from typing import List, Dict, Optional
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Task:
    """A simple task data structure created with AI assistance."""
    id: int
    title: str
    description: str
    completed: bool = False
    created_at: datetime = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()
    
    def mark_complete(self) -> None:
        """Mark the task as completed."""
        self.completed = True
    
    def to_dict(self) -> Dict:
        """Convert task to dictionary representation."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed,
            'created_at': self.created_at.isoformat()
        }


class TaskManager:
    """A simple task management system demonstrating AI-assisted programming."""
    
    def __init__(self):
        self.tasks: List[Task] = []
        self.next_id = 1
    
    def add_task(self, title: str, description: str = "") -> Task:
        """Add a new task to the manager."""
        task = Task(
            id=self.next_id,
            title=title,
            description=description
        )
        self.tasks.append(task)
        self.next_id += 1
        return task
    
    def get_task(self, task_id: int) -> Optional[Task]:
        """Retrieve a task by its ID."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def complete_task(self, task_id: int) -> bool:
        """Mark a task as completed."""
        task = self.get_task(task_id)
        if task:
            task.mark_complete()
            return True
        return False
    
    def get_pending_tasks(self) -> List[Task]:
        """Get all tasks that are not completed."""
        return [task for task in self.tasks if not task.completed]
    
    def get_completed_tasks(self) -> List[Task]:
        """Get all completed tasks."""
        return [task for task in self.tasks if task.completed]
    
    def export_to_json(self, filename: str) -> None:
        """Export all tasks to a JSON file."""
        data = {
            'tasks': [task.to_dict() for task in self.tasks],
            'exported_at': datetime.now().isoformat()
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    def generate_report(self) -> str:
        """Generate a summary report of all tasks."""
        total = len(self.tasks)
        completed = len(self.get_completed_tasks())
        pending = len(self.get_pending_tasks())
        
        report = f"""
        Task Management Report
        =====================
        Total Tasks: {total}
        Completed: {completed}
        Pending: {pending}
        Completion Rate: {(completed/total*100 if total > 0 else 0):.1f}%
        
        Recent Tasks:
        """
        
        # Show last 5 tasks
        recent_tasks = sorted(self.tasks, key=lambda t: t.created_at, reverse=True)[:5]
        for task in recent_tasks:
            status = "✓" if task.completed else "○"
            report += f"        {status} {task.title}\n"
        
        return report


def demonstrate_ai_patterns():
    """Demonstrate various AI programming patterns."""
    
    # Create a task manager
    tm = TaskManager()
    
    # Add some sample tasks
    tm.add_task("Learn GitHub Copilot", "Understand how to use AI for programming")
    tm.add_task("Complete Lab 01", "Finish the introduction to AI tools lab")
    tm.add_task("Practice AI debugging", "Use AI to help identify and fix code issues")
    tm.add_task("Build a small project", "Apply AI programming skills to a real project")
    
    # Complete some tasks
    tm.complete_task(1)
    tm.complete_task(2)
    
    # Generate and print report
    print(tm.generate_report())
    
    # Export data
    tm.export_to_json("tasks.json")
    print("Tasks exported to tasks.json")


if __name__ == "__main__":
    demonstrate_ai_patterns()