from datetime import datetime
import csv
import os

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


def view_tasks():
    """This functions reads tasks from csv and displays them"""
    tasks = []

    if os.path.exists('tasks.csv'):
        with open ('tasks.csv', 'a', newline='') as f:
            reader = csv.reader(f)

            for row in reader:
                description, due_date, priority, completed = row
                task = Task(description, due_date, priority, completed == "True")
                tasks.append(task)
            print(tasks)
    # sort by due date
    tasks.sort(key=lambda t: t.due_date)

    for idx, task in enumerate(tasks, start=1):
        print(f'{idx}. {task}')


def mark_tasks_complete(task_index):
    """Marks tasks as complete"""
    tasks = []

    with open('tasks.csv', 'r', newline='') as f:
        reader = csv.reader(f)
        tasks = list(reader)

        if 0 <= task_index < len(tasks):
            tasks[task_index][3] == "True"

            with open('tasks.csv', 'w', newline=''):
                writer = csv.writer(f)
                writer.writerows(tasks)
            print(f'Task {task_index + 1} marked as complete')
        else:
            print('Invalid task number')