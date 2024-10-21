import os
import json

class TaskManager:  
    def __init__(self):
        self.pathToTasks = "tasks.json"
        self.tasks = []
        self.loadTasks()
        self.loop()

    def loadTasks(self):
    # Check if the file exists to avoid FileNotFoundError
        if os.path.exists(self.pathToTasks):
            with open(self.pathToTasks, 'r') as file:
                try:
                    self.tasks = json.load(file)
                    print("Tasks loaded successfully!")
                except json.JSONDecodeError:
                    print("Error loading tasks. The file may be corrupted.")
        else:
            print("No tasks file found. Starting with an empty task list.")



    def writeTask(self):
        with open(self.pathToTasks,'w') as file:
            json.dump(self.tasks,file,indent=4)
        print("Tasks saved successfully!")

    def addTask(self):
        title = input("Enter task title: ")
        deadline = input("Enter task deadline (DD-MM-HH-MM): ")
        task = {"title": title, "deadline": deadline}
        self.tasks.append(task)
        print("Task added successfully!")

    def viewTasks(self):
        if not self.tasks:
            print("No tasks yet!")
            return
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task['title']} - Deadline: {task['deadline']}")

    def editTask(self):
        if not self.tasks:
            print("No tasks available.")
            return

        while True:
            num = input("Enter task number (0 to cancel): ")
            if num.isdigit():
                num = int(num)
            else:
                print("Invalid Input. Try again.")
                continue

            if num == 0:
                return
            elif 1 <= num <= len(self.tasks):
                break
            else:
                print("Invalid task number. Try again.")

        # Update the task
        new_title = input("Enter new task title (leave blank to keep current): ")
        new_deadline = input("Enter new deadline (DD-MM-HH-MM) or leave blank to keep current: ")

        if new_title:
            self.tasks[num - 1]["title"] = new_title
        if new_deadline:
            self.tasks[num - 1]["deadline"] = new_deadline

        print("Task updated successfully!")

    def delTask(self):
        if not self.tasks:
            print("No tasks available for deleting.")
            return

       

        while True:
            num = input("Enter task number to be deleted (0 to cancel): ")
            if num.isdigit():
                num = int(num)
            else:
                print("Invalid Input. Try again.")
                continue

            if num == 0:
                return
            elif 1 <= num <= len(self.tasks):
                break
            else:
                print("Invalid task number. Try again.")

            
        del self.tasks[num-1]


    def handleInput(self):
        choice = input()
        match choice:
            case "1":
                self.addTask()
            case "2":
                self.viewTasks()
            case "3":
                self.editTask()
            case "4":
                self.delTask()
            case "5":
                self.writeTask()
                print("Exiting Task Manager. Goodbye!")
                exit(0)
            case _:
                print("Invalid Input!\n")

    def printMenu(self):
        print("\n*____Task Manager Menu____*")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Save and Exit")

    def loop(self):
        while True:
            self.printMenu()
            self.handleInput()

def main():
    TaskManager()
    return 0

if __name__ == "__main__":
    main()
