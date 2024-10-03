from datetime import datetime
import csv
import os
import argparse

class Task:
    """A model to store task details"""
    def __init__(self, description, due_date, priority, completed=False):
        self.description = description
        try:
            self.due_date = datetime.strptime(due_date, '%Y-%m-%d')
        except ValueError:
            raise ValueError(f'Incorrect data format {due_date}. It should be YYYY-MM-DD')
        self.priority = priority
        self.completed = completed


    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f'{self.description} | Due: {self.due_date.date()} | Priority: {self.priority} | Status: {status}'
    
def add_task(description, due_date, priority):
    """A function to add tasks to a csv file"""
    try:
        task = Task(description, due_date, priority)
    except ValueError as e:
        print(e)
        return
    
    with open('tasks.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([description, due_date, priority, task.completed])
    print(task)
    print(f"Task: {description} added successfully")


def view_tasks():
    """This functions reads tasks from csv and displays them"""
    tasks = []

    if not os.path.exists('tasks.csv'):
        print('No tasks found. Please add a task first')
        return


    with open ('tasks.csv', 'r') as f:
        reader = csv.reader(f)

        for row in reader:
            try:
                description, due_date, priority, completed = row
            except ValueError:
                print('No tasks added yet')
                return
            task = Task(description, due_date, priority, completed == 'True')
            tasks.append(task)
    
    if not tasks:
        print("No tasks available")
        return
    
    # sort by due date
    tasks.sort(key=lambda t: t.due_date)

    for idx, task in enumerate(tasks, start=1):
        print(f'{idx}. {task}')


def mark_tasks_complete(task_index):
    """Marks tasks as complete"""
    tasks = []

    if not os.path.exists('tasks.csv'):
        print('No tasks available. Add a task first')
        return

    with open('tasks.csv', 'r', newline='') as f:
        reader = csv.reader(f)
        tasks = list(reader)

    if 0 <= task_index < len(tasks):
        tasks[task_index][3] = "True"

        with open('tasks.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(tasks)
        print(f'Task {task_index + 1} marked as complete')
    else:
        print('No such task. View tasks available by number')


def delete_task(task_index):
    """Deletes a task by index"""
    if not os.path.exists('tasks.csv'):
        print("Tasks not found")
        return
    
    tasks = []
    
    with open('tasks.csv', mode='r', newline='') as f:
        reader = csv.reader(f)
        tasks = list(reader)

    if 0 <= task_index < len(tasks):
        deleted_task = tasks.pop(task_index)

        with open('tasks.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(tasks)
        print(f'Deleted {deleted_task[0]}')
    else:
        print(f"Invalid task number. Please select a task number between 1 and {len(tasks)}")



def parse_arguments():
    parser = argparse.ArgumentParser(description="A CLI Task Manager")

    parser.add_argument(
        '--add', nargs=3, metavar=('description', 'due_date', 'priority'),
        help='Add a new task(due data format: YYYY-MM-DD)')
    parser.add_argument('--view', action='store_true', help='Displays all tasks')
    parser.add_argument('--complete', type=int, help="Mark completed tasks as complete")
    parser.add_argument('--delete', type=int, help="Delete a task by number")

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()

    if args.add:
        description, due_date, priority = args.add
        add_task(description, due_date, priority)
    elif args.view:
        view_tasks()
    elif args.complete is not None:
        mark_tasks_complete(args.complete - 1)
    elif args.delete is not None:
        delete_task(args.delete - 1)