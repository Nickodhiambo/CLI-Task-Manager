# A Command Line Based Task Manager

A **command-line tool** that manages tasks for users. This tool allows a user to add,
view, mark as complete, and delete tasks. Additionally, a user can use the tool to check
which tasks are due within the next 2 days. Moreover, the CLI tool allows users to categorize
tasks and designate the important ones. This command line tool, incorporating a colorized and well-formated output, caters to both technical and non-technical users. It can be useful as a task tracking and organization assistant for team leaders charged with assigning duties and responsibilities to juniors, or for personal use.

## Features
- **Adding tasks**: Users can add tasks by providing a task's description, due date, task priority, and, optionally, passing a category in which a task belongs.
- **viewing tasks**: Users can view task entries, which are automatically stored in a csv file when
a task is added. When a user requests to view tasks, various information about each task — Description, Due Date, Priority, Category(Tags) and status (Whether completed or not) are displayed
- **Marking completed tasks**: Users can mark tasks as completed by simply passing the task's number to a command, and a task with that number will be updated as "Done"
- **Deleting tasks**: For completed tasks, users can choose to delete them by passing in the task number to a command.
- **Task Tagging**: Users can categorize tasks for easier identification by passing a tag to a task when adding the task
- **Friendly Error Messages**: The program is user friendly. It implements error handling mechanisms that displays friendly and easy to understand error messages for non-technical users.
- **Colorized Output Messages**: This tool uses color codes to display different outputs for successful operations and errors.

## How It Works

The tool allows you to pass specific flags from the command line to invoke various task management
functionalities. To use a command, you run the `task_manager.py` script from a terminal, appending a command you wish to execute. You can run `python task_manager.py --help` to view all the available commands.

### Command-Line Arguments

| `--add`                                | Adds a task entry                                         |
| `--view`                               | Views all tasks                                           |
| `--complete`                           | Marks a task as complete                                  |
| `--delete`                             | Deletes a task                                            |
| `--reminders`                          | Checks tasks that are due within 2 days                   |

## Installation

To use this tool, follow these steps:

1. Clone this repository:

   ```bash
   git clone https://github.com/Nickodhiambo/CLI-Task-Manager.git
   ```

2. Create and activate a Python virtual environment
    ```bash
    python -m venv venv
    <!-- For windows -->
    venv\Scripts\activate

    <!-- For linux -->
    source venv/bin/activate
    ```

3. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Change into project directory
   ```bash
   cd CLI-Task-Manager
   ```

## Usage

Run the tool using your favorite terminal, by specifying the flag corresponding to the function you want to execute.

### Examples

**1. Add a Task with a Category**
```bash
python task_manager.py --add "Buy Groceries" "2024-10-09" "High" "Shopping"
```
You are adding a task described as 'Buy groceries' under a category called 'Shopping'. The task's priority(importance) is set to 'High'. Note that you must provide a description, due date and priority

**2. Add a Task without a Category**
```bash
python task_manager.py --add "Buy Groceries" "2024-10-09" "High"
```
You are adding a task described as 'Buy groceries' without a category. The category field will be empty.

**3. View all tasks**
```bash
python task_manager.py --view
```
Displays all tasks in a numbered format, starting from the earliest added task

**4. Check upcoming tasks**
```bash
python task_manager.py --reminders
```
Displays all tasks due in 2 days

**5. Mark tasks as complete**
```bash
python task_manager.py --complete 1
```
Mark a task numbered 1 as complete. You must pass in the task number which you can obtain by viewing all tasks.

**6. Delete a task**
```bash
python task_manager.py --delete 1
```
Deletes a task assigned number 1. You must pass in the task number to delete

## Contributing

If you'd like to contribute, please fork the repository and submit a pull request. Feel free to suggest new features or report bugs through the issue tracker.

## Acknowledgments

Special thanks to all the developers and open-source projects that made this tool possible.

---