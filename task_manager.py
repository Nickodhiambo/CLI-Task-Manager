import datetime
import csv

class Task:
    """A model to store task details"""
    def __init__(self, description, due_date, priority, completed=False):
        self.description = description
        self.due_date = datetime.strptime(due_date, '%Y-%m-%d')
        self.priority = priority
        self.completed = completed


    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f'{self.description} | Due: {self.due_date.date()} | Priority: {self.priority} | Status: {status}'
    
def add_task(description, due_date, priority):
    """A function to add tasks to a csv file"""
    task = Task(description, due_date, priority)
    with open('tasks.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerows([description, due_date, priority, task.completed])
    print(f'Task {description} added successfully')