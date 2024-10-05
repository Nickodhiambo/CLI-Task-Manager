from datetime import datetime
import csv
import os
import argparse

class Task:
    """A model to store task details"""
    def __init__(self, description, due_date, priority, tags="", completed=False):
        self.description = description
        try:
            self.due_date = datetime.strptime(due_date, '%Y-%m-%d')
        except ValueError:
            raise ValueError(f'Incorrect data format {due_date}. It should be YYYY-MM-DD')
        self.priority = priority
        self.tags = tags
        self.completed = completed


    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f'{self.description} | Due: {self.due_date.date()} | Priority: {self.priority} | Tags: {self.tags} | Status: {status}'
    
def add_task(description, due_date, priority, tags=""):
    """A function to add tasks to a csv file"""
    try:
        task = Task(description, due_date, priority, tags)
    except ValueError as e:
        print(e)
        return
    
    file_exists = os.path.exists('tasks.csv')
    with open('tasks.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['Description', 'Due Date', 'Priority', 'Tags', 'Completed'])
        writer.writerow([description, due_date, priority, tags, task.completed])
    print(f"Task: {description} added successfully under {tags}")


def view_tasks():
    """This functions reads tasks from csv and displays them"""
    tasks = []

    if not os.path.exists('tasks.csv'):
        print('No tasks found. Please add a task first')
        return


    with open ('tasks.csv', 'r') as f:
        reader = list(csv.reader(f))

        for row in reader[1:]:
            try:
                description, due_date, priority, tags, completed = row
            except ValueError:
                print('No tasks added yet')
                return
            task = Task(description, due_date, priority, tags, completed == 'True')
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

    if 1 <= task_index < len(tasks):
        tasks[task_index][4] = "True"

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

    if 1 <= task_index < len(tasks):
        deleted_task = tasks.pop(task_index)

        with open('tasks.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(tasks)
        print(f'Deleted {deleted_task[0]} due on {deleted_task[1]}')
    else:
        print(f"Invalid task number. Please select a task number between 1 and {len(tasks)}")



def parse_arguments():
    parser = argparse.ArgumentParser(description="A CLI Task Manager")

    parser.add_argument(
        '--add', nargs='+', help='Add a new task(due data format: YYYY-MM-DD), optional tags')
    parser.add_argument('--view', action='store_true', help='Displays all tasks')
    parser.add_argument('--complete', type=int, help="Mark completed tasks as complete")
    parser.add_argument('--delete', type=int, help="Delete a task by number")

    return parser.parse_args()

def main():
    args = parse_arguments()

    if args.add:
        print(args.add)
        if len(args.add) < 3:
            print("Please provide a task description, due date and priority")
            return
        description = args.add[0]
        due_date = args.add[1]
        priority = args.add[2]
        tags = ''.join(args.add[3] if len(args.add) > 3 else "")
        
        add_task(description, due_date, priority, tags)
    elif args.view:
        view_tasks()
    elif args.complete is not None:
        mark_tasks_complete(args.complete - 1)
    elif args.delete is not None:
        delete_task(args.delete - 1)

if __name__ == "__main__":
    main()