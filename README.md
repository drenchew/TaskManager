Task Manager
A simple command-line task management application written in Python, designed to help you keep track of tasks with deadlines. The app supports adding, viewing, editing, and deleting tasks, as well as saving them to a file for persistence.

Features
Add Tasks: Create tasks with titles and deadlines in the DD-MM-HH-MM format (Day-Month-Hour-Minute).
View Tasks: Display a list of tasks with their titles and deadlines.
Edit Tasks: Modify the title and deadline of existing tasks.
Delete Tasks: Remove tasks from the list.
Save Tasks: Save tasks to a tasks.json file to maintain them across sessions.
Load Tasks: Automatically loads tasks from tasks.json on startup.
Technologies
Python: The application is developed using standard Python libraries.
JSON: Used for saving and loading tasks to a file.
os: For file handling and checking the existence of the tasks file.
re (optional): Can be used for validating the deadline format.
Getting Started
Prerequisites

Python 3.x should be installed on your system.
Clone the Repository

bash
Copy code
git clone https://github.com/yourusername/TaskManager.git
cd TaskManager
Run the Application

bash
Copy code
python TaskManager.py
Usage
When you start the application, it will load tasks from tasks.json if the file exists.
The menu will display options:
markdown
Copy code
*____Task Manager Menu____*
1. Add Task
2. List Tasks
3. Edit Task
4. Delete Task
5. Save and Exit
Choose an option by entering the corresponding number.
Task Deadline Format
The deadline for each task should be entered in the format DD-MM-HH-MM:

DD: Day
MM: Month
HH: Hour
MM: Minute
Example: 10-10-12-30 represents the 10th day of the 10th month at 12:30.

File Structure
TaskManager.py: The main script that contains all the functionalities.
tasks.json: The file where tasks are saved. It will be created automatically if it doesn't exist.
Example Workflow
Add a task
Enter task title: Buy groceries
Enter task deadline: 15-10-10-00
View tasks
Output:
markdown
Copy code
1. Buy groceries - Deadline: 15-10-10-00
Edit a task
Enter task number: 1
Update title and/or deadline as needed.
Delete a task
Enter task number: 1 (to remove the first task).
Save and exit
Tasks are saved to tasks.json.
Known Issues
The application currently doesn't support time zone conversions or advanced scheduling features.
Input validation for the deadline format could be enhanced for stricter checking.
Contributing
Feel free to open issues and submit pull requests. For major changes, please open a discussion first to communicate what you would like to change.

License
This project is open-source and available under the MIT License.

